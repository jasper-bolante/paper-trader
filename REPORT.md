# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-27 23:02 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,791.71** |
| Total return since inception | -1.04% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,746.33 (3.73%) |
| Positions value | $17,024.46 |
| Settled cash | $2,761.86 |
| Unsettled cash (T+1) | $13.91 |
| Tax reserve | $8.52 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.11% | 3.55% |
| Annualized volatility | 11.93% | 12.35% |
| Sharpe (rf 4%) | -0.93 | 1.71 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 37 | 37 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $25.93 | $725.90 | $-37.71 | $25.00 |
| BBY | 14 | $88.05 | $83.59 | $1,170.33 | $-62.42 | $80.33 |
| CRL | 2 | $285.12 | $296.02 | $592.04 | $21.80 | $268.70 |
| CSX | 17 | $50.29 | $51.52 | $875.84 | $20.89 | $46.58 |
| EXPE | 2 | $331.47 | $319.03 | $638.06 | $-24.88 | $305.24 |
| FDS | 2 | $299.76 | $304.88 | $609.76 | $10.23 | $274.51 |
| HUM | 2 | $406.24 | $392.50 | $785.01 | $-27.46 | $357.63 |
| IQV | 2 | $255.46 | $262.18 | $524.36 | $13.45 | $235.96 |
| MPC | 3 | $306.56 | $363.25 | $1,089.75 | $170.07 | $330.10 |
| NTAP | 4 | $187.95 | $190.59 | $762.36 | $10.57 | $174.52 |
| PANW | 2 | $388.17 | $382.71 | $765.42 | $-10.92 | $344.44 |
| PSX | 5 | $215.50 | $239.84 | $1,199.20 | $121.72 | $219.13 |
| SPY | 5 | $743.10 | $770.83 | $3,854.15 | $138.65 | — |
| STT | 8 | $185.86 | $193.28 | $1,546.24 | $59.37 | $174.19 |
| VEEV | 3 | $250.82 | $282.18 | $846.54 | $94.07 | $253.96 |
| VLO | 3 | $304.72 | $346.50 | $1,039.50 | $125.34 | $315.01 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-879.32 | $0.00 | $554.53 |

Dividends received: $56.77. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-27T23:02` system **EXPE** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-27T23:02` system — corporate_actions_synced
- `2026-08-26T21:00` system — eod_complete
- `2026-08-26T18:18` no_trade — no signals crossed action thresholds this hour
- `2026-08-26T18:18` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
