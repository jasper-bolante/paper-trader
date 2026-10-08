# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-08 19:23 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,390.12** |
| Total return since inception | 1.95% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,920.47 (4.60%) |
| Positions value | $18,658.71 |
| Settled cash | $1,736.45 |
| Unsettled cash (T+1) | $9.44 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.48% | 4.42% |
| Annualized volatility | 11.05% | 11.18% |
| Sharpe (rf 4%) | 0.22 | 1.22 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 65 | 65 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| AMD | 1 | $650.00 | $616.19 | $616.19 | $-33.81 | $581.31 |
| ANET | 4 | $191.78 | $211.24 | $844.94 | $77.82 | $194.20 |
| APA | 19 | $44.15 | $45.88 | $871.62 | $32.74 | $39.73 |
| CRL | 3 | $296.67 | $293.49 | $880.47 | $-9.55 | $279.86 |
| FFIV | 2 | $448.44 | $462.34 | $924.68 | $27.79 | $423.09 |
| IQV | 2 | $255.46 | $258.07 | $516.14 | $5.23 | $247.54 |
| META | 1 | $723.49 | $719.02 | $719.02 | $-4.47 | $650.61 |
| MPC | 3 | $399.06 | $467.27 | $1,401.81 | $204.64 | $398.12 |
| NTAP | 5 | $206.27 | $230.55 | $1,152.75 | $121.40 | $212.25 |
| PSX | 5 | $215.50 | $282.58 | $1,412.90 | $335.42 | $246.58 |
| RVTY | 9 | $122.75 | $151.54 | $1,363.86 | $259.14 | $141.67 |
| SPY | 5 | $743.10 | $773.50 | $3,867.53 | $152.03 | — |
| TECH | 12 | $72.32 | $72.48 | $869.76 | $1.92 | $65.36 |
| VLO | 3 | $392.61 | $446.35 | $1,339.05 | $161.23 | $381.71 |
| WST | 2 | $370.69 | $364.25 | $728.50 | $-12.88 | $339.09 |
| ZBRA | 3 | $345.13 | $383.16 | $1,149.48 | $114.10 | $347.47 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,124.61 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-08T19:23` no_trade — no signals crossed action thresholds this hour
- `2026-10-08T19:23` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-07T23:43` system — eod_complete
- `2026-10-07T19:28` entry buy **META** — momentum entry: rank 20, mom 0.344, vol 47%
- `2026-10-07T19:28` entry buy **AMD** — momentum entry: rank 2, mom 1.073, vol 49%
- `2026-10-07T19:28` no_trade skip_entry **TMO** — sector cap: Health Care would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **MSFT** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **A** — sector cap: Health Care would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **PLTR** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **HPQ** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **DDOG** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **FTNT** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **MU** — insufficient investable cash (size $929, need >= $500)
- `2026-10-06T23:11` system — eod_complete
- `2026-10-06T19:00` no_trade skip_entry **WAT** — insufficient investable cash (size $311, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
