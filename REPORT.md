# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-18 20:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,863.26** |
| Total return since inception | -0.68% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,652.67 (3.26%) |
| Positions value | $17,831.31 |
| Settled cash | $2,029.92 |
| Unsettled cash (T+1) | $9.95 |
| Tax reserve | $7.92 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.75% | 3.08% |
| Annualized volatility | 12.31% | 13.37% |
| Sharpe (rf 4%) | -0.80 | 1.74 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 30 | 30 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $25.94 | $726.32 | $-37.29 | $25.00 |
| BBY | 14 | $88.05 | $87.30 | $1,222.13 | $-10.62 | $79.24 |
| CNC | 8 | $75.27 | $65.22 | $521.80 | $-80.33 | $58.73 |
| CRL | 2 | $285.12 | $279.30 | $558.59 | $-11.65 | $258.00 |
| CSX | 17 | $50.29 | $50.23 | $853.91 | $-1.04 | $46.01 |
| FTNT | 7 | $149.43 | $157.86 | $1,105.02 | $58.98 | $151.44 |
| HUM | 2 | $398.00 | $381.93 | $763.85 | $-32.14 | $350.32 |
| MPC | 3 | $306.56 | $366.78 | $1,100.34 | $180.66 | $330.10 |
| NTAP | 5 | $161.48 | $204.81 | $1,024.05 | $216.67 | $186.39 |
| NUE | 2 | $269.82 | $264.41 | $528.82 | $-10.82 | $245.50 |
| PANW | 2 | $388.28 | $374.15 | $748.30 | $-28.26 | $349.27 |
| PSX | 5 | $215.50 | $243.47 | $1,217.38 | $139.89 | $219.13 |
| SPY | 5 | $743.10 | $767.35 | $3,836.75 | $121.25 | — |
| STT | 8 | $185.86 | $191.88 | $1,535.04 | $48.17 | $173.64 |
| VLO | 3 | $304.72 | $350.01 | $1,050.03 | $135.87 | $315.01 |
| WST | 3 | $336.32 | $346.33 | $1,038.99 | $30.03 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $52.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-18T19:50` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T19:50` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T19:08` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T19:08` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T17:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T17:56` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T16:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T16:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T15:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T15:58` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T15:03` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T15:03` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T14:08` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T14:08` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T14:07` system **PSX** — cash settles on pay date; 15% dividend tax reserved

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
