"""Daily signal computation, cached in the DB (computed once per trading
day on the first hourly run, reused by later runs).

Signals use daily bars through the PREVIOUS close — no lookahead.
Momentum: blended 3m/6m return, skipping the most recent week (short-term
reversal noise). Trend filter: price above a rising 50DMA. Eligibility:
price, liquidity, and volatility gates from config.
"""
import math
import statistics
from datetime import date, timedelta

from . import universe


def ensure(conn, api, cfg, today, prev_trading_day):
    """Compute signals for `today` if not already done. Returns signal date."""
    row = conn.execute(
        "SELECT COUNT(*) AS n FROM signals WHERE signal_date=?", (today,)
    ).fetchone()
    if row["n"] > 0:
        return today

    symbols = [u["symbol"] for u in universe.load()]
    scfg, ucfg = cfg["signals"], cfg["universe"]
    need = scfg["momentum_long_days"] + scfg["momentum_skip_days"] + 10
    start = (date.fromisoformat(today) - timedelta(days=int(need * 1.7) + 30)).isoformat()
    end = f"{prev_trading_day}T23:59:59Z"
    bars = api.daily_bars(symbols, f"{start}T00:00:00Z", end)

    computed = []
    for sym in symbols:
        b = bars.get(sym) or []
        closes = [x["c"] for x in b]
        vols = [x["v"] for x in b]
        sig = _compute_one(sym, closes, vols, scfg, ucfg)
        computed.append(sig)

    eligible = [s for s in computed if s["eligible"]]
    eligible.sort(key=lambda s: s["momentum"], reverse=True)
    ranks = {s["symbol"]: i + 1 for i, s in enumerate(eligible)}

    for s in computed:
        conn.execute(
            "INSERT OR REPLACE INTO signals(signal_date,symbol,momentum,rank,"
            "price,ma_trend,ma_trend_rising,ma_exit,adv_dollar,ann_vol,"
            "eligible,veto_reason) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (today, s["symbol"], s["momentum"], ranks.get(s["symbol"]),
             s["price"], s["ma_trend"], s["ma_trend_rising"], s["ma_exit"],
             s["adv_dollar"], s["ann_vol"], int(s["eligible"]), s["veto"]),
        )
    conn.commit()
    return today


def _compute_one(sym, closes, vols, scfg, ucfg):
    out = {"symbol": sym, "momentum": None, "price": None, "ma_trend": None,
           "ma_trend_rising": None, "ma_exit": None, "adv_dollar": None,
           "ann_vol": None, "eligible": False, "veto": None}
    skip = scfg["momentum_skip_days"]
    long_d = scfg["momentum_long_days"]
    short_d = scfg["momentum_short_days"]
    if len(closes) < long_d + skip + 6:
        out["veto"] = f"insufficient history ({len(closes)} bars)"
        return out

    price = closes[-1]
    ref = closes[-1 - skip]
    mom = 0.5 * (ref / closes[-1 - skip - short_d] - 1) \
        + 0.5 * (ref / closes[-1 - skip - long_d] - 1)
    ma_trend = statistics.fmean(closes[-scfg["trend_ma_days"]:])
    lb = scfg["ma_rising_lookback"]
    ma_trend_prev = statistics.fmean(closes[-scfg["trend_ma_days"] - lb:-lb])
    rising = ma_trend > ma_trend_prev
    ma_exit = statistics.fmean(closes[-scfg["exit_ma_days"]:])
    adv_dollar = statistics.fmean(c * v for c, v in zip(closes[-20:], vols[-20:]))
    rets = [closes[i] / closes[i - 1] - 1 for i in range(len(closes) - 30, len(closes))]
    ann_vol = statistics.pstdev(rets) * math.sqrt(252) if len(rets) > 5 else None

    out.update(momentum=round(mom, 6), price=price, ma_trend=round(ma_trend, 4),
               ma_trend_rising=int(rising), ma_exit=round(ma_exit, 4),
               adv_dollar=round(adv_dollar, 2),
               ann_vol=round(ann_vol, 4) if ann_vol else None)

    if price < ucfg["min_price"]:
        out["veto"] = f"price {price} < min {ucfg['min_price']}"
    elif adv_dollar < ucfg["min_avg_dollar_volume"]:
        out["veto"] = f"ADV$ {adv_dollar:.0f} below liquidity floor"
    elif ann_vol is None or ann_vol > ucfg["max_annualized_vol"]:
        out["veto"] = f"volatility {ann_vol} above cap {ucfg['max_annualized_vol']}"
    elif price <= ma_trend:
        out["veto"] = "below 50DMA (trend filter)"
    elif not rising:
        out["veto"] = "50DMA not rising"
    else:
        out["eligible"] = True
    return out


def get_all(conn, signal_date):
    rows = conn.execute(
        "SELECT * FROM signals WHERE signal_date=?", (signal_date,)
    ).fetchall()
    return {r["symbol"]: dict(r) for r in rows}


def latest_date(conn):
    row = conn.execute("SELECT MAX(signal_date) AS d FROM signals").fetchone()
    return row["d"]
