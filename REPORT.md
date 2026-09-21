# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-21 18:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,006.33** |
| Total return since inception | 0.03% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,525.64 (2.63%) |
| Positions value | $18,965.40 |
| Settled cash | $1,029.50 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.19% | 2.45% |
| Annualized volatility | 11.39% | 11.63% |
| Sharpe (rf 4%) | -0.38 | 0.74 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 52 | 52 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $205.47 | $821.86 | $54.74 | $179.57 |
| APA | 19 | $44.15 | $44.15 | $838.85 | $-0.04 | $39.73 |
| BBY | 8 | $101.21 | $93.41 | $747.24 | $-62.44 | $85.09 |
| CNC | 16 | $71.60 | $65.43 | $1,046.88 | $-98.74 | $59.53 |
| CRL | 3 | $296.67 | $278.06 | $834.16 | $-55.86 | $256.69 |
| GEN | 40 | $29.13 | $29.32 | $1,172.80 | $7.54 | $26.22 |
| IQV | 2 | $255.46 | $269.64 | $539.28 | $28.37 | $244.26 |
| MPC | 3 | $306.56 | $413.62 | $1,240.86 | $321.18 | $382.13 |
| NTAP | 5 | $206.27 | $197.52 | $987.60 | $-43.75 | $179.40 |
| PSX | 5 | $215.50 | $265.61 | $1,328.05 | $250.57 | $246.58 |
| RVTY | 9 | $122.75 | $143.34 | $1,290.02 | $185.30 | $132.06 |
| SPY | 5 | $743.10 | $774.32 | $3,871.60 | $156.10 | — |
| TECH | 12 | $72.32 | $72.47 | $869.64 | $1.80 | $65.20 |
| TGT | 7 | $162.82 | $158.35 | $1,108.45 | $-31.26 | $147.91 |
| VLO | 3 | $304.72 | $403.90 | $1,211.70 | $297.54 | $371.72 |
| ZBRA | 3 | $345.13 | $352.13 | $1,056.40 | $21.02 | $313.44 |

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
