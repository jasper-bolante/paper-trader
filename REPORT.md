# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-21 22:46 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,894.24** |
| Total return since inception | -0.53% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,810.39 (4.05%) |
| Positions value | $18,853.31 |
| Settled cash | $1,029.50 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.60% | 3.87% |
| Annualized volatility | 11.32% | 11.88% |
| Sharpe (rf 4%) | -0.55 | 1.27 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 53 | 53 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $205.66 | $822.62 | $55.50 | $185.09 |
| APA | 19 | $44.15 | $43.81 | $832.39 | $-6.50 | $39.73 |
| BBY | 8 | $101.21 | $93.19 | $745.56 | $-64.12 | $85.09 |
| CNC | 16 | $71.60 | $64.96 | $1,039.36 | $-106.26 | $59.53 |
| CRL | 3 | $296.67 | $279.09 | $837.27 | $-52.75 | $256.69 |
| GEN | 40 | $29.13 | $29.16 | $1,166.40 | $1.14 | $26.24 |
| IQV | 2 | $255.46 | $270.04 | $540.08 | $29.17 | $244.26 |
| MPC | 3 | $306.56 | $401.88 | $1,205.64 | $285.96 | $382.13 |
| NTAP | 5 | $206.27 | $198.19 | $990.97 | $-40.38 | $179.40 |
| PSX | 5 | $215.50 | $261.77 | $1,308.85 | $231.37 | $246.58 |
| RVTY | 9 | $122.75 | $143.60 | $1,292.40 | $187.68 | $132.06 |
| SPY | 5 | $743.10 | $773.21 | $3,866.05 | $150.55 | — |
| TECH | 12 | $72.32 | $72.44 | $869.28 | $1.44 | $65.20 |
| TGT | 7 | $162.82 | $157.69 | $1,103.83 | $-35.88 | $147.91 |
| VLO | 3 | $304.72 | $393.30 | $1,179.90 | $265.74 | $371.72 |
| ZBRA | 3 | $345.13 | $350.90 | $1,052.70 | $17.32 | $315.81 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,107.74 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-21T18:52` entry buy **APA** — momentum entry: rank 15, mom 0.274, vol 44%
- `2026-09-21T18:52` no_trade skip_entry **TMO** — sector cap: Health Care would exceed 25% of equity
- `2026-09-21T18:52` no_trade skip_entry **WAT** — insufficient investable cash (size $854, need >= $500)
- `2026-09-18T22:46` system — eod_complete
- `2026-09-18T22:46` system **SPY** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-18T22:46` system — corporate_actions_synced
- `2026-09-18T19:54` no_trade — no signals crossed action thresholds this hour
- `2026-09-18T19:54` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-09-18T17:09` entry buy **GEN** — momentum entry: rank 10, mom 0.314, vol 33%
- `2026-09-18T17:09` entry buy **CNC** — momentum entry: rank 8, mom 0.412, vol 36%
- `2026-09-17T21:39` system — eod_complete
- `2026-09-17T17:43` entry buy **ZBRA** — momentum entry: rank 4, mom 0.548, vol 26%
- `2026-09-17T17:43` entry buy **CRL** — momentum entry: rank 3, mom 0.565, vol 42%
- `2026-09-17T17:43` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-17T17:43` exit sell **GPC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
