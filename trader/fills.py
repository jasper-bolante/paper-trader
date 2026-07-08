"""Fill simulation. No order ever fills instantly at the quoted mid.

Model:
- Buys pay the ask, sells receive the bid. If no sane quote is available
  (IEX can gap on thin names), a fallback spread is synthesized around the
  last trade.
- Market impact uses a square-root model: impact = k * daily_vol *
  sqrt(order_value / average_daily_dollar_volume). Negligible for small
  orders in liquid names, grows with size and volatility.
- Fills are capped at a participation fraction of actual traded volume in
  the window; the remainder stays working.
- Resting limit orders fill only if price trades THROUGH the limit
  (touching exactly is not enough — models queue position).
- Stop orders trigger on the first bar whose low breaches the stop; if the
  bar OPENS below the stop (gap), the fill bases off the open, not the
  stop — you eat the gap, like real life.
"""
import math
from dataclasses import dataclass


@dataclass
class FillResult:
    qty: float
    price: float
    spread_cost: float  # $ paid crossing the spread vs mid
    impact_cost: float  # $ paid to market impact
    note: str = ""


def _sane_half_spread(bid, ask, cfg):
    """Half-spread as a fraction of mid, or None if the quote is unusable."""
    if bid and ask and 0 < bid < ask:
        mid = (bid + ask) / 2
        hs = (ask - bid) / 2 / mid
        if hs <= cfg["fills"]["max_half_spread_bps"] / 1e4:
            return hs
    return None


def effective_prices(quote, cfg):
    """(mid, buy_side_price, sell_side_price) before impact."""
    bid = quote.get("bid")
    ask = quote.get("ask")
    last = quote.get("last")
    hs = _sane_half_spread(bid, ask, cfg)
    if hs is not None:
        return (bid + ask) / 2, ask, bid
    ref = last or ask or bid
    if not ref or ref <= 0:
        return None, None, None
    hs = cfg["fills"]["fallback_half_spread_bps"] / 1e4
    return ref, ref * (1 + hs), ref * (1 - hs)


def impact_fraction(order_value, adv_dollar, ann_vol, cfg):
    if not adv_dollar or adv_dollar <= 0 or order_value <= 0:
        return 0.0
    daily_vol = (ann_vol if ann_vol and ann_vol > 0 else 0.25) / math.sqrt(252)
    return cfg["fills"]["impact_coefficient"] * daily_vol * math.sqrt(
        order_value / adv_dollar
    )


def participation_cap(qty, window_volume, cfg):
    """Max shares fillable against observed volume. None = volume unknown."""
    if window_volume is None:
        return qty
    cap = math.floor(window_volume * cfg["fills"]["max_participation"])
    return min(qty, cap)


def fill_market(side, qty, quote, adv_dollar, ann_vol, window_volume, cfg):
    """Immediate marketable fill. Returns FillResult (qty may be partial/0)."""
    mid, buy_px, sell_px = effective_prices(quote, cfg)
    if mid is None:
        return FillResult(0, 0, 0, 0, "no usable quote")
    fill_qty = participation_cap(qty, window_volume, cfg)
    if fill_qty <= 0:
        return FillResult(0, 0, 0, 0, "no liquidity in window")
    base = buy_px if side == "buy" else sell_px
    imp = impact_fraction(fill_qty * mid, adv_dollar, ann_vol, cfg)
    price = base * (1 + imp) if side == "buy" else base * (1 - imp)
    spread_cost = abs(base - mid) * fill_qty
    impact_cost = abs(price - base) * fill_qty
    note = "partial: volume cap" if fill_qty < qty else ""
    return FillResult(fill_qty, round(price, 4), round(spread_cost, 4),
                      round(impact_cost, 4), note)


def evaluate_limit(side, qty, limit_price, quote, bars, adv_dollar, ann_vol, cfg):
    """Resting limit order vs current quote + bars since last check.

    Marketable now -> fills at the touch (never worse than limit).
    Otherwise requires a trade-through in the bar history.
    """
    mid, buy_px, sell_px = effective_prices(quote, cfg)
    if mid is not None:
        if side == "buy" and buy_px is not None and buy_px <= limit_price:
            res = fill_market("buy", qty, quote, adv_dollar, ann_vol,
                              _bars_volume(bars), cfg)
            if res.qty > 0:
                res.price = min(res.price, limit_price)
                return res
        if side == "sell" and sell_px is not None and sell_px >= limit_price:
            res = fill_market("sell", qty, quote, adv_dollar, ann_vol,
                              _bars_volume(bars), cfg)
            if res.qty > 0:
                res.price = max(res.price, limit_price)
                return res
    # Trade-through check on bars since the order was last evaluated.
    through = [
        b for b in bars
        if (side == "buy" and b["l"] < limit_price)
        or (side == "sell" and b["h"] > limit_price)
    ]
    if not through:
        return FillResult(0, 0, 0, 0, "not reached")
    vol = sum(b["v"] for b in through)
    fill_qty = participation_cap(qty, vol, cfg)
    if fill_qty <= 0:
        return FillResult(0, 0, 0, 0, "reached but no volume")
    note = "partial: volume cap" if fill_qty < qty else ""
    return FillResult(fill_qty, limit_price, 0.0, 0.0, note)


def evaluate_stop(side, qty, stop_price, quote, bars, adv_dollar, ann_vol, cfg):
    """Stop order (sell stops for our strategy). Trigger then fill as market,
    honoring gaps through the stop."""
    trigger_base = None
    trigger_note = ""
    for b in bars:
        breached = b["l"] <= stop_price if side == "sell" else b["h"] >= stop_price
        if breached:
            if side == "sell" and b["o"] < stop_price:
                trigger_base = b["o"]  # gapped below the stop: fill off the open
                trigger_note = f"gap through stop (open {b['o']})"
            elif side == "buy" and b["o"] > stop_price:
                trigger_base = b["o"]
                trigger_note = f"gap through stop (open {b['o']})"
            else:
                trigger_base = stop_price
            break
    if trigger_base is None:
        last = quote.get("last")
        if last is not None and (
            (side == "sell" and last <= stop_price)
            or (side == "buy" and last >= stop_price)
        ):
            trigger_base = min(stop_price, last) if side == "sell" else max(stop_price, last)
    if trigger_base is None:
        return FillResult(0, 0, 0, 0, "not triggered")

    hs_quote = dict(quote)
    hs_quote.setdefault("last", trigger_base)
    # Price off the trigger base, paying spread + impact from there.
    mid, buy_px, sell_px = effective_prices({"last": trigger_base}, cfg)
    vol = _bars_volume(bars)
    fill_qty = participation_cap(qty, vol, cfg)
    if fill_qty <= 0:
        return FillResult(0, 0, 0, 0, "triggered but no volume")
    imp = impact_fraction(fill_qty * trigger_base, adv_dollar, ann_vol, cfg)
    base = sell_px if side == "sell" else buy_px
    price = base * (1 - imp) if side == "sell" else base * (1 + imp)
    spread_cost = abs(base - trigger_base) * fill_qty
    impact_cost = abs(price - base) * fill_qty
    note = ("partial: volume cap; " if fill_qty < qty else "") + trigger_note
    return FillResult(fill_qty, round(price, 4), round(spread_cost, 4),
                      round(impact_cost, 4), note.strip("; "))


def _bars_volume(bars):
    if not bars:
        return None
    return sum(b["v"] for b in bars)
