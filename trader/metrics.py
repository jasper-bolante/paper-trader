"""Risk/performance metrics from end-of-day equity snapshots."""
import math
import statistics


def series(conn):
    rows = conn.execute(
        "SELECT snap_date, equity, benchmark_value FROM equity_snapshots "
        "WHERE kind='eod' ORDER BY snap_date"
    ).fetchall()
    return [(r["snap_date"], r["equity"], r["benchmark_value"]) for r in rows]


def _stats(values, cfg):
    out = {"total_return": None, "ann_vol": None, "sharpe": None,
           "max_drawdown": None}
    values = [v for v in values if v is not None]
    if len(values) < 2:
        if values:
            out["total_return"] = 0.0
        return out
    tdy = cfg["metrics"]["trading_days_per_year"]
    rf_daily = cfg["metrics"]["risk_free_rate"] / tdy
    rets = [values[i] / values[i - 1] - 1 for i in range(1, len(values))]
    out["total_return"] = values[-1] / values[0] - 1
    if len(rets) >= 2:
        sd = statistics.stdev(rets)
        out["ann_vol"] = sd * math.sqrt(tdy)
        if sd > 0:
            out["sharpe"] = (statistics.fmean(rets) - rf_daily) / sd * math.sqrt(tdy)
    peak, mdd = values[0], 0.0
    for v in values:
        peak = max(peak, v)
        mdd = max(mdd, 1 - v / peak)
    out["max_drawdown"] = mdd
    return out


def compute(conn, cfg):
    s = series(conn)
    return {
        "days": len(s),
        "portfolio": _stats([e for _, e, _ in s], cfg),
        "benchmark": _stats([b for _, _, b in s], cfg),
    }
