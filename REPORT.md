# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-19 17:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,778.62** |
| Total return since inception | -1.11% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,652.67 (3.26%) |
| Positions value | $17,641.47 |
| Settled cash | $1,366.98 |
| Unsettled cash (T+1) | $778.54 |
| Tax reserve | $8.37 |

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
| BAX | 28 | $27.27 | $26.59 | $744.66 | $-18.95 | $25.00 |
| BBY | 14 | $88.05 | $89.19 | $1,248.73 | $15.98 | $79.24 |
| CNC | 8 | $75.27 | $64.94 | $519.52 | $-82.61 | $58.73 |
| CRL | 2 | $285.12 | $289.26 | $578.52 | $8.28 | $258.00 |
| CSX | 17 | $50.29 | $50.86 | $864.62 | $9.67 | $46.01 |
| EXPE | 2 | $331.47 | $330.07 | $660.14 | $-2.80 | $298.17 |
| FTNT | 7 | $149.43 | $153.54 | $1,074.78 | $28.74 | $151.44 |
| MPC | 3 | $306.56 | $361.26 | $1,083.78 | $164.10 | $330.10 |
| NTAP | 5 | $161.48 | $197.75 | $988.77 | $181.39 | $186.39 |
| NUE | 2 | $269.82 | $249.84 | $499.68 | $-39.96 | $245.50 |
| PANW | 2 | $388.28 | $358.70 | $717.40 | $-59.16 | $349.27 |
| PSX | 5 | $215.50 | $242.42 | $1,212.10 | $134.62 | $219.13 |
| SPY | 5 | $743.10 | $769.69 | $3,848.45 | $132.95 | — |
| STT | 8 | $185.86 | $188.08 | $1,504.64 | $17.77 | $173.64 |
| VLO | 3 | $304.72 | $344.17 | $1,032.51 | $118.35 | $315.01 |
| WST | 3 | $336.32 | $354.39 | $1,063.17 | $54.21 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-931.39 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-19T17:52` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T17:52` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-19T16:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T16:57` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-19T15:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T15:59` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-19T15:03` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T15:03` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-19T14:08` entry buy **EXPE** — momentum entry: rank 9, mom 0.404, vol 42%
- `2026-08-19T14:08` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-19T14:08` system **MPC** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-18T20:52` system — eod_complete
- `2026-08-18T19:50` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T19:50` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T19:08` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
