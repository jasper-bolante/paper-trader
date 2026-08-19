# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-19 16:57 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,813.63** |
| Total return since inception | -0.93% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,652.67 (3.26%) |
| Positions value | $17,676.48 |
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
| BAX | 28 | $27.27 | $26.52 | $742.56 | $-21.05 | $25.00 |
| BBY | 14 | $88.05 | $89.13 | $1,247.82 | $15.07 | $79.24 |
| CNC | 8 | $75.27 | $64.80 | $518.40 | $-83.73 | $58.73 |
| CRL | 2 | $285.12 | $289.94 | $579.87 | $9.63 | $258.00 |
| CSX | 17 | $50.29 | $51.09 | $868.62 | $13.66 | $46.01 |
| EXPE | 2 | $331.47 | $331.29 | $662.58 | $-0.36 | $298.17 |
| FTNT | 7 | $149.43 | $153.36 | $1,073.52 | $27.48 | $151.44 |
| MPC | 3 | $306.56 | $362.03 | $1,086.09 | $166.41 | $330.10 |
| NTAP | 5 | $161.48 | $198.50 | $992.52 | $185.14 | $186.39 |
| NUE | 2 | $269.82 | $260.19 | $520.37 | $-19.27 | $245.50 |
| PANW | 2 | $388.28 | $358.03 | $716.06 | $-60.50 | $349.27 |
| PSX | 5 | $215.50 | $242.53 | $1,212.65 | $135.17 | $219.13 |
| SPY | 5 | $743.10 | $769.72 | $3,848.60 | $133.10 | — |
| STT | 8 | $185.86 | $188.99 | $1,511.92 | $25.05 | $173.64 |
| VLO | 3 | $304.72 | $344.76 | $1,034.30 | $120.14 | $315.01 |
| WST | 3 | $336.32 | $353.54 | $1,060.61 | $51.64 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-931.39 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-18T19:08` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T17:56` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
