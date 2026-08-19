# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-19 14:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,859.92** |
| Total return since inception | -0.70% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,652.67 (3.26%) |
| Positions value | $17,722.76 |
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
| BAX | 28 | $27.27 | $26.63 | $745.64 | $-17.97 | $25.00 |
| BBY | 14 | $88.05 | $89.70 | $1,255.80 | $23.05 | $79.24 |
| CNC | 8 | $75.27 | $64.93 | $519.44 | $-82.69 | $58.73 |
| CRL | 2 | $285.12 | $292.23 | $584.45 | $14.21 | $258.00 |
| CSX | 17 | $50.29 | $51.51 | $875.59 | $20.63 | $46.01 |
| EXPE | 2 | $331.47 | $331.30 | $662.59 | $-0.35 | $298.17 |
| FTNT | 7 | $149.43 | $152.18 | $1,065.26 | $19.22 | $151.44 |
| MPC | 3 | $306.56 | $362.30 | $1,086.88 | $167.21 | $330.10 |
| NTAP | 5 | $161.48 | $199.07 | $995.35 | $187.97 | $186.39 |
| NUE | 2 | $269.82 | $265.23 | $530.46 | $-9.18 | $245.50 |
| PANW | 2 | $388.28 | $355.06 | $710.12 | $-66.44 | $349.27 |
| PSX | 5 | $215.50 | $242.38 | $1,211.88 | $134.39 | $219.13 |
| SPY | 5 | $743.10 | $769.74 | $3,848.70 | $133.20 | — |
| STT | 8 | $185.86 | $190.91 | $1,527.28 | $40.41 | $173.64 |
| VLO | 3 | $304.72 | $345.82 | $1,037.47 | $123.31 | $315.01 |
| WST | 3 | $336.32 | $355.29 | $1,065.86 | $56.89 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-931.39 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-18T16:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T15:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T15:58` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T15:03` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
