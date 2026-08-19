# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-19 15:59 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,823.08** |
| Total return since inception | -0.88% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,652.67 (3.26%) |
| Positions value | $17,685.93 |
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
| BAX | 28 | $27.27 | $26.55 | $743.26 | $-20.35 | $25.00 |
| BBY | 14 | $88.05 | $88.99 | $1,245.86 | $13.11 | $79.24 |
| CNC | 8 | $75.27 | $64.47 | $515.72 | $-86.41 | $58.73 |
| CRL | 2 | $285.12 | $290.28 | $580.56 | $10.32 | $258.00 |
| CSX | 17 | $50.29 | $51.14 | $869.38 | $14.43 | $46.01 |
| EXPE | 2 | $331.47 | $332.25 | $664.50 | $1.56 | $298.17 |
| FTNT | 7 | $149.43 | $153.59 | $1,075.10 | $29.06 | $151.44 |
| MPC | 3 | $306.56 | $363.03 | $1,089.09 | $169.41 | $330.10 |
| NTAP | 5 | $161.48 | $197.60 | $988.00 | $180.62 | $186.39 |
| NUE | 2 | $269.82 | $260.73 | $521.45 | $-18.19 | $245.50 |
| PANW | 2 | $388.28 | $359.70 | $719.40 | $-57.16 | $349.27 |
| PSX | 5 | $215.50 | $242.92 | $1,214.60 | $137.12 | $219.13 |
| SPY | 5 | $743.10 | $770.52 | $3,852.62 | $137.12 | — |
| STT | 8 | $185.86 | $187.98 | $1,503.84 | $16.97 | $173.64 |
| VLO | 3 | $304.72 | $345.89 | $1,037.67 | $123.51 | $315.01 |
| WST | 3 | $336.32 | $354.96 | $1,064.88 | $55.92 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-931.39 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-18T17:56` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T16:59` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
