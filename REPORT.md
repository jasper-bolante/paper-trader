# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-26 14:20 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,634.55** |
| Total return since inception | -1.83% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,612.30 (3.06%) |
| Positions value | $16,868.10 |
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
| BAX | 28 | $27.27 | $26.46 | $741.02 | $-22.59 | $25.00 |
| BBY | 14 | $88.05 | $86.72 | $1,214.08 | $-18.67 | $80.33 |
| CRL | 2 | $285.12 | $299.19 | $598.38 | $28.14 | $268.70 |
| CSX | 17 | $50.29 | $52.05 | $884.93 | $29.98 | $46.44 |
| EXPE | 2 | $331.47 | $337.85 | $675.70 | $12.76 | $305.24 |
| FDS | 2 | $299.76 | $293.73 | $587.45 | $-12.08 | $274.51 |
| HUM | 2 | $406.24 | $397.37 | $794.74 | $-17.73 | $357.63 |
| IQV | 2 | $255.46 | $259.93 | $519.85 | $8.94 | $234.27 |
| MPC | 3 | $306.56 | $357.91 | $1,073.73 | $154.05 | $330.10 |
| NTAP | 4 | $187.95 | $190.66 | $762.66 | $10.87 | $169.07 |
| PANW | 2 | $388.17 | $339.31 | $678.62 | $-97.72 | $322.11 |
| PSX | 5 | $215.50 | $239.44 | $1,197.20 | $119.72 | $219.13 |
| SPY | 5 | $743.10 | $765.96 | $3,829.78 | $114.28 | — |
| STT | 8 | $185.86 | $193.16 | $1,545.32 | $58.45 | $173.74 |
| VEEV | 3 | $250.82 | $246.51 | $739.54 | $-12.93 | $225.63 |
| VLO | 3 | $304.72 | $341.70 | $1,025.10 | $110.94 | $315.01 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-879.32 | $0.00 | $554.53 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-25T15:23` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T15:23` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
