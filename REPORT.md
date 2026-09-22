# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-22 17:43 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,850.56** |
| Total return since inception | -0.75% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,810.39 (4.05%) |
| Positions value | $18,809.62 |
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
| ANET | 4 | $191.78 | $203.91 | $815.64 | $48.52 | $185.09 |
| APA | 19 | $44.15 | $43.05 | $817.86 | $-21.03 | $39.73 |
| BBY | 8 | $101.21 | $95.08 | $760.64 | $-49.04 | $85.09 |
| CNC | 16 | $71.60 | $63.67 | $1,018.72 | $-126.90 | $59.53 |
| CRL | 3 | $296.67 | $288.60 | $865.80 | $-24.22 | $256.69 |
| GEN | 40 | $29.13 | $27.14 | $1,085.40 | $-79.86 | $26.24 |
| IQV | 2 | $255.46 | $270.81 | $541.62 | $30.71 | $244.26 |
| MPC | 3 | $306.56 | $404.20 | $1,212.62 | $292.94 | $382.13 |
| NTAP | 5 | $206.27 | $193.09 | $965.45 | $-65.90 | $179.40 |
| PSX | 5 | $215.50 | $263.90 | $1,319.50 | $242.02 | $246.58 |
| RVTY | 9 | $122.75 | $143.21 | $1,288.89 | $184.17 | $132.06 |
| SPY | 5 | $743.10 | $773.38 | $3,866.90 | $151.40 | — |
| TECH | 12 | $72.32 | $72.63 | $871.56 | $3.72 | $65.20 |
| TGT | 7 | $162.82 | $159.81 | $1,118.67 | $-21.04 | $147.91 |
| VLO | 3 | $304.72 | $394.01 | $1,182.05 | $267.89 | $371.72 |
| ZBRA | 3 | $345.13 | $359.44 | $1,078.32 | $42.94 | $315.81 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,107.74 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-22T17:43` no_trade — no signals crossed action thresholds this hour
- `2026-09-22T17:43` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-09-21T22:46` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
