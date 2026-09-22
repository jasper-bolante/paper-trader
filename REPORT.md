# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-22 21:36 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,697.94** |
| Total return since inception | -1.51% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,809.58 (4.05%) |
| Positions value | $18,657.01 |
| Settled cash | $1,029.50 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.58% | 3.86% |
| Annualized volatility | 11.41% | 11.77% |
| Sharpe (rf 4%) | -0.96 | 1.25 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 54 | 54 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $205.30 | $821.20 | $54.08 | $185.09 |
| APA | 19 | $44.15 | $42.31 | $803.89 | $-35.00 | $39.73 |
| BBY | 8 | $101.21 | $94.84 | $758.72 | $-50.96 | $85.36 |
| CNC | 16 | $71.60 | $63.29 | $1,012.64 | $-132.98 | $59.53 |
| CRL | 3 | $296.67 | $285.10 | $855.30 | $-34.72 | $256.69 |
| GEN | 40 | $29.13 | $27.30 | $1,092.00 | $-73.26 | $26.24 |
| IQV | 2 | $255.46 | $270.10 | $540.20 | $29.29 | $244.26 |
| MPC | 3 | $306.56 | $389.84 | $1,169.52 | $249.84 | $382.13 |
| NTAP | 5 | $206.27 | $192.89 | $964.45 | $-66.90 | $179.40 |
| PSX | 5 | $215.50 | $256.75 | $1,283.78 | $206.30 | $246.58 |
| RVTY | 9 | $122.75 | $143.32 | $1,289.88 | $185.16 | $132.06 |
| SPY | 5 | $743.10 | $773.18 | $3,865.90 | $150.40 | — |
| TECH | 12 | $72.32 | $72.55 | $870.60 | $2.76 | $65.30 |
| TGT | 7 | $162.82 | $159.02 | $1,113.14 | $-26.57 | $147.91 |
| VLO | 3 | $304.72 | $377.22 | $1,131.66 | $217.50 | $371.72 |
| ZBRA | 3 | $345.13 | $361.38 | $1,084.14 | $48.76 | $325.24 |

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
