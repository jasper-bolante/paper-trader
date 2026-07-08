"""Alpaca REST client (market data + trading calendar). Free tier:
real-time quotes/bars from the IEX feed; historical SIP data available
except the most recent 15 minutes. We use SIP for daily history (signals)
and IEX for anything recent (quotes, minute bars, fills).
"""
import os
import time
import requests

DATA_BASE = "https://data.alpaca.markets"
TRADING_BASE = "https://paper-api.alpaca.markets"


class AlpacaError(Exception):
    pass


class AlpacaData:
    def __init__(self, key_id=None, secret=None):
        self.key_id = key_id or os.environ.get("ALPACA_API_KEY_ID")
        self.secret = secret or os.environ.get("ALPACA_API_SECRET_KEY")
        if not self.key_id or not self.secret:
            raise AlpacaError(
                "Missing ALPACA_API_KEY_ID / ALPACA_API_SECRET_KEY env vars"
            )
        self.session = requests.Session()
        self.session.headers.update({
            "APCA-API-KEY-ID": self.key_id,
            "APCA-API-SECRET-KEY": self.secret,
            "Accept": "application/json",
        })

    def _get(self, url, params=None, tries=4):
        for attempt in range(tries):
            resp = self.session.get(url, params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            if resp.status_code == 429 or resp.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            raise AlpacaError(f"GET {url} -> {resp.status_code}: {resp.text[:300]}")
        raise AlpacaError(f"GET {url} -> retries exhausted")

    @staticmethod
    def _chunks(symbols, n=100):
        symbols = list(symbols)
        for i in range(0, len(symbols), n):
            yield symbols[i:i + n]

    def latest_quotes(self, symbols):
        """{symbol: {bid, ask, bid_size, ask_size, ts}} from IEX."""
        out = {}
        for chunk in self._chunks(symbols):
            js = self._get(f"{DATA_BASE}/v2/stocks/quotes/latest",
                           {"symbols": ",".join(chunk), "feed": "iex"})
            for sym, q in (js.get("quotes") or {}).items():
                out[sym] = {"bid": q.get("bp"), "ask": q.get("ap"),
                            "bid_size": q.get("bs"), "ask_size": q.get("as"),
                            "ts": q.get("t")}
        return out

    def latest_trades(self, symbols):
        out = {}
        for chunk in self._chunks(symbols):
            js = self._get(f"{DATA_BASE}/v2/stocks/trades/latest",
                           {"symbols": ",".join(chunk), "feed": "iex"})
            for sym, t in (js.get("trades") or {}).items():
                out[sym] = {"price": t.get("p"), "ts": t.get("t")}
        return out

    def _bars(self, symbols, timeframe, start, end, feed, adjustment="split",
              limit=10000):
        out = {s: [] for s in symbols}
        for chunk in self._chunks(symbols, 50):
            params = {
                "symbols": ",".join(chunk), "timeframe": timeframe,
                "start": start, "end": end, "adjustment": adjustment,
                "feed": feed, "limit": limit, "sort": "asc",
            }
            token = None
            while True:
                if token:
                    params["page_token"] = token
                js = self._get(f"{DATA_BASE}/v2/stocks/bars", params)
                for sym, bars in (js.get("bars") or {}).items():
                    out[sym].extend(
                        {"t": b["t"], "o": b["o"], "h": b["h"], "l": b["l"],
                         "c": b["c"], "v": b["v"]} for b in bars
                    )
                token = js.get("next_page_token")
                if not token:
                    break
        return out

    def daily_bars(self, symbols, start, end):
        """Split-adjusted daily bars. SIP history; falls back to IEX if the
        key isn't entitled to SIP for the requested range."""
        try:
            return self._bars(symbols, "1Day", start, end, feed="sip")
        except AlpacaError:
            return self._bars(symbols, "1Day", start, end, feed="iex")

    def minute_bars(self, symbols, start_iso, end_iso):
        return self._bars(symbols, "1Min", start_iso, end_iso, feed="iex",
                          adjustment="raw")

    def corporate_actions(self, symbols, start, end):
        """Normalized: [{symbol, type, ex_date, pay_date, rate, raw}]."""
        results = []
        for chunk in self._chunks(symbols, 50):
            params = {"symbols": ",".join(chunk),
                      "types": "cash_dividend,forward_split,reverse_split",
                      "start": start, "end": end, "limit": 1000}
            token = None
            while True:
                if token:
                    params["page_token"] = token
                js = self._get(f"{DATA_BASE}/v1/corporate-actions", params)
                ca = js.get("corporate_actions") or {}
                for d in ca.get("cash_dividends", []):
                    results.append({
                        "symbol": d.get("symbol"), "type": "cash_dividend",
                        "ex_date": d.get("ex_date"),
                        "pay_date": d.get("payable_date") or d.get("pay_date"),
                        "rate": d.get("rate"), "raw": d,
                    })
                for s in ca.get("forward_splits", []):
                    new, old = s.get("new_rate"), s.get("old_rate")
                    results.append({
                        "symbol": s.get("symbol"), "type": "forward_split",
                        "ex_date": s.get("ex_date"), "pay_date": None,
                        "rate": (new / old) if new and old else None, "raw": s,
                    })
                for s in ca.get("reverse_splits", []):
                    new, old = s.get("new_rate"), s.get("old_rate")
                    results.append({
                        "symbol": s.get("symbol"), "type": "reverse_split",
                        "ex_date": s.get("ex_date"), "pay_date": None,
                        "rate": (new / old) if new and old else None, "raw": s,
                    })
                token = js.get("next_page_token")
                if not token:
                    break
        return [r for r in results if r["symbol"] and r["ex_date"] and r["rate"]]

    def calendar(self, start, end):
        """[{date, open, close}] trading days including early closes."""
        js = self._get(f"{TRADING_BASE}/v2/calendar", {"start": start, "end": end})
        return [{"date": d["date"], "open": d["open"], "close": d["close"]}
                for d in js]

    def clock(self):
        return self._get(f"{TRADING_BASE}/v2/clock")
