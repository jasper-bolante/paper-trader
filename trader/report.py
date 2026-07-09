"""REPORT.md + docs/equity_curve.svg — the human-readable performance view,
regenerated at each end-of-day run and committed to the repo. GitHub renders
both, so checking performance = opening REPORT.md in the repo."""
import json
import os
from datetime import datetime, timezone

from . import config, dashboard, db, ledger, metrics, tax


def _pct(x, digits=2):
    return f"{x * 100:.{digits}f}%" if x is not None else "—"


def _usd(x):
    return f"${x:,.2f}" if x is not None else "—"


def generate(conn, cfg, last_prices, today, api=None):
    positions = ledger.positions(conn)
    settled = ledger.settled_cash(conn, today)
    total_cash = ledger.total_cash(conn)
    unsettled = round(total_cash - settled, 2)
    reserve = tax.tax_reserve(conn, cfg)
    pos_value = sum(
        p["qty"] * (last_prices.get(s) or 0) for s, p in positions.items()
    )
    equity = round(total_cash + pos_value - reserve, 2)
    start_cash = cfg["account"]["starting_cash"]
    m = metrics.compute(conn, cfg)
    bench_row = conn.execute(
        "SELECT benchmark_value FROM equity_snapshots WHERE kind='eod' "
        "AND benchmark_value IS NOT NULL ORDER BY snap_date DESC LIMIT 1"
    ).fetchone()
    bench_value = bench_row["benchmark_value"] if bench_row else None

    lines = []
    lines.append("# Paper Trading Account — Performance Report")
    lines.append("")
    url = (cfg.get("reporting") or {}).get("dashboard_url")
    if url:
        lines.append(f"**➜ [Interactive dashboard]({url})** — hover/click any "
                     f"term to learn what it means, toggle the chart lines, "
                     f"and browse full trade history.")
        lines.append("")
    lines.append(f"_Updated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} · "
                 f"inception {db.get_meta(conn, 'inception') or '—'} · "
                 f"drawdown state: **{db.get_meta(conn, 'dd_state') or 'normal'}**_")
    lines.append("")
    lines.append("![equity curve](docs/equity_curve.svg)")
    lines.append("")
    lines.append("## Account")
    lines.append("")
    lines.append("| | |")
    lines.append("|---|---:|")
    lines.append(f"| **Equity (net of tax reserve)** | **{_usd(equity)}** |")
    lines.append(f"| Total return since inception | {_pct(equity / start_cash - 1)} |")
    lines.append(f"| S&P 500 benchmark (same $ , dividends reinvested) | {_usd(bench_value)} "
                 f"({_pct(bench_value / start_cash - 1) if bench_value else '—'}) |")
    lines.append(f"| Positions value | {_usd(round(pos_value, 2))} |")
    lines.append(f"| Settled cash | {_usd(settled)} |")
    lines.append(f"| Unsettled cash (T+1) | {_usd(unsettled)} |")
    lines.append(f"| Tax reserve | {_usd(reserve)} |")
    lines.append("")

    lines.append("## Risk-adjusted metrics")
    lines.append("")
    lines.append("| Metric | Portfolio | Benchmark |")
    lines.append("|---|---:|---:|")
    p, b = m["portfolio"], m["benchmark"]
    lines.append(f"| Total return | {_pct(p['total_return'])} | {_pct(b['total_return'])} |")
    lines.append(f"| Annualized volatility | {_pct(p['ann_vol'])} | {_pct(b['ann_vol'])} |")
    sharpe_p = f"{p['sharpe']:.2f}" if p["sharpe"] is not None else "—"
    sharpe_b = f"{b['sharpe']:.2f}" if b["sharpe"] is not None else "—"
    lines.append(f"| Sharpe (rf {_pct(cfg['metrics']['risk_free_rate'], 0)}) | {sharpe_p} | {sharpe_b} |")
    lines.append(f"| Max drawdown | {_pct(p['max_drawdown'])} | {_pct(b['max_drawdown'])} |")
    lines.append(f"| EOD observations | {m['days']} | {m['days']} |")
    lines.append("")

    lines.append("## Positions")
    lines.append("")
    if positions:
        lines.append("| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|")
        for sym in sorted(positions):
            pos = positions[sym]
            last = last_prices.get(sym)
            val = pos["qty"] * last if last else None
            avg = pos["basis"] / pos["qty"]
            unreal = (val - pos["basis"]) if val is not None else None
            st = conn.execute("SELECT stop_price FROM position_state WHERE symbol=?",
                              (sym,)).fetchone()
            stop = _usd(st["stop_price"]) if st else "—"
            lines.append(f"| {sym} | {pos['qty']:g} | {_usd(avg)} | {_usd(last)} | "
                         f"{_usd(val)} | {_usd(unreal)} | {stop} |")
    else:
        lines.append("_No open positions._")
    lines.append("")

    lines.append("## Realized gains & tax")
    lines.append("")
    summary = tax.realized_summary(conn)
    if summary:
        lines.append("| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | ")
        lines.append("|---|---:|---:|---:|")
        for yr in sorted(summary):
            wash = conn.execute(
                "SELECT COALESCE(SUM(wash_disallowed),0) AS w FROM realized "
                "WHERE substr(trade_date,1,4)=?", (yr,),
            ).fetchone()["w"]
            lines.append(f"| {yr} | {_usd(summary[yr]['short'])} | "
                         f"{_usd(summary[yr]['long'])} | {_usd(wash)} |")
    else:
        lines.append("_No realized gains yet._")
    div = tax.dividends_received(conn)
    lines.append("")
    lines.append(f"Dividends received: {_usd(div)}. Assumed rates: "
                 f"{_pct(cfg['tax']['short_term_rate'], 0)} short-term, "
                 f"{_pct(cfg['tax']['long_term_rate'], 0)} long-term, "
                 f"{_pct(cfg['tax']['dividend_rate'], 0)} dividends, no state tax.")
    lines.append("")

    lines.append("## Recent decisions")
    lines.append("")
    rows = conn.execute(
        "SELECT * FROM decisions WHERE kind IN "
        "('entry','exit','no_trade','halt','system') "
        "ORDER BY id DESC LIMIT 15"
    ).fetchall()
    for r in rows:
        try:
            d = json.loads(r["detail"])
            why = d.get("reason") or d.get("note") or d.get("event") or ""
        except (ValueError, TypeError):
            why = ""
        sym = f" **{r['symbol']}**" if r["symbol"] else ""
        act = f" {r['action']}" if r["action"] else ""
        lines.append(f"- `{r['ts'][:16]}` {r['kind']}{act}{sym} — {why}")
    lines.append("")
    lines.append("_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_")

    with open(os.path.join(config.ROOT, "REPORT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    _equity_svg(conn, cfg)
    dashboard.generate(conn, cfg, last_prices, today, api=api)


def _equity_svg(conn, cfg):
    s = metrics.series(conn)
    os.makedirs(os.path.join(config.ROOT, "docs"), exist_ok=True)
    path = os.path.join(config.ROOT, "docs", "equity_curve.svg")
    w, h, pad = 900, 420, 55
    if len(s) < 2:
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">'
               f'<text x="{w//2}" y="{h//2}" text-anchor="middle" '
               f'font-family="sans-serif" fill="#888">Equity curve appears after '
               f'two end-of-day snapshots</text></svg>')
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        return
    eq = [(d, e) for d, e, _ in s]
    bm = [(d, b) for d, b, _ in s if b is not None]
    vals = [e for _, e in eq] + [b for _, b in bm]
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1.0
    lo -= span * 0.05
    hi += span * 0.05

    def pts(series_):
        n = len(eq)
        idx = {d: i for i, (d, _) in enumerate(eq)}
        out = []
        for d, v in series_:
            i = idx.get(d)
            if i is None:
                continue
            x = pad + i * (w - 2 * pad) / max(1, n - 1)
            y = h - pad - (v - lo) * (h - 2 * pad) / (hi - lo)
            out.append(f"{x:.1f},{y:.1f}")
        return " ".join(out)

    grid = []
    for k in range(5):
        v = lo + (hi - lo) * k / 4
        y = h - pad - (v - lo) * (h - 2 * pad) / (hi - lo)
        grid.append(f'<line x1="{pad}" y1="{y:.0f}" x2="{w-pad}" y2="{y:.0f}" '
                    f'stroke="#e0e0e0"/>'
                    f'<text x="{pad-8}" y="{y:.0f}" text-anchor="end" '
                    f'dominant-baseline="middle" font-size="11" fill="#888" '
                    f'font-family="sans-serif">${v:,.0f}</text>')
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'style="background:#fff">'
        + "".join(grid)
        + f'<polyline points="{pts(bm)}" fill="none" stroke="#999" '
          f'stroke-width="1.5" stroke-dasharray="4 3"/>'
        + f'<polyline points="{pts(eq)}" fill="none" stroke="#1668c8" '
          f'stroke-width="2.2"/>'
        + f'<text x="{pad}" y="22" font-size="13" font-family="sans-serif" '
          f'fill="#1668c8">— Portfolio</text>'
        + f'<text x="{pad+110}" y="22" font-size="13" font-family="sans-serif" '
          f'fill="#999">- - SPY buy &amp; hold</text>'
        + f'<text x="{pad}" y="{h-18}" font-size="11" font-family="sans-serif" '
          f'fill="#888">{eq[0][0]}</text>'
        + f'<text x="{w-pad}" y="{h-18}" text-anchor="end" font-size="11" '
          f'font-family="sans-serif" fill="#888">{eq[-1][0]}</text>'
        + "</svg>"
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
