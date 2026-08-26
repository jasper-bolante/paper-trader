# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-26 16:02 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,680.04** |
| Total return since inception | -1.60% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,612.30 (3.06%) |
| Positions value | $16,913.60 |
| Settled cash | $1,716.01 |
| Unsettled cash (T+1) | $1,058.80 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.26% | 2.88% |
| Annualized volatility | 12.03% | 12.65% |
| Sharpe (rf 4%) | -1.68 | 1.41 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 35 | 35 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.52 | $742.70 | $-20.91 | $25.00 |
| BBY | 14 | $88.05 | $87.26 | $1,221.64 | $-11.11 | $80.33 |
| CRL | 2 | $285.12 | $296.45 | $592.91 | $22.67 | $268.70 |
| CSX | 17 | $50.29 | $52.02 | $884.42 | $29.47 | $46.44 |
| EXPE | 2 | $331.47 | $336.30 | $672.60 | $9.66 | $305.24 |
| FDS | 2 | $299.76 | $292.26 | $584.53 | $-15.00 | $274.51 |
| HUM | 2 | $406.24 | $389.61 | $779.22 | $-33.25 | $357.63 |
| IQV | 2 | $255.46 | $261.35 | $522.70 | $11.79 | $234.27 |
| MPC | 3 | $306.56 | $363.38 | $1,090.12 | $170.45 | $330.10 |
| NTAP | 4 | $187.95 | $192.21 | $768.82 | $17.03 | $169.07 |
| PANW | 2 | $388.17 | $338.60 | $677.20 | $-99.14 | $322.11 |
| PSX | 5 | $215.50 | $243.06 | $1,215.30 | $137.82 | $219.13 |
| SPY | 5 | $743.10 | $765.03 | $3,825.15 | $109.65 | — |
| STT | 8 | $185.86 | $194.31 | $1,554.52 | $67.65 | $173.74 |
| VEEV | 3 | $250.82 | $246.89 | $740.67 | $-11.80 | $225.63 |
| VLO | 3 | $304.72 | $347.03 | $1,041.09 | $126.93 | $315.01 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-879.32 | $0.00 | $554.53 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-26T16:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-26T16:02` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-26T14:20` entry buy **HUM** — momentum entry: rank 4, mom 0.657, vol 38%
- `2026-08-26T14:20` exit sell **WST** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-25T20:57` system — eod_complete
- `2026-08-25T19:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T19:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T19:09` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T19:09` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T17:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T17:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T17:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T17:07` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T16:09` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T16:09` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
