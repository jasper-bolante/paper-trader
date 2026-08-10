# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-10 14:38 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,603.10** |
| Total return since inception | -1.98% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,809.04 (4.05%) |
| Positions value | $18,562.99 |
| Settled cash | $1,043.31 |
| Unsettled cash (T+1) | $3.60 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.50% | 3.86% |
| Annualized volatility | 11.65% | 14.76% |
| Sharpe (rf 4%) | -3.79 | 2.74 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 23 | 23 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.49 | $769.72 | $6.11 | $24.79 |
| BBY | 14 | $88.05 | $81.83 | $1,145.62 | $-87.13 | $79.24 |
| CSCO | 8 | $131.57 | $123.81 | $990.52 | $-62.07 | $109.28 |
| CSX | 17 | $50.29 | $50.33 | $855.53 | $0.58 | $46.01 |
| DDOG | 3 | $268.94 | $250.01 | $750.03 | $-56.79 | $211.93 |
| DOC | 40 | $21.90 | $21.08 | $843.20 | $-32.87 | $18.97 |
| FTNT | 7 | $149.43 | $165.94 | $1,161.55 | $115.51 | $151.44 |
| HPQ | 31 | $28.20 | $30.20 | $936.35 | $62.11 | $27.04 |
| HUM | 2 | $398.00 | $386.74 | $773.48 | $-22.51 | $348.07 |
| MPC | 3 | $306.56 | $310.58 | $931.74 | $12.06 | $287.83 |
| NTAP | 5 | $161.48 | $200.34 | $1,001.70 | $194.32 | $172.38 |
| PSX | 5 | $215.50 | $210.12 | $1,050.60 | $-26.88 | $191.32 |
| SPY | 5 | $743.10 | $774.39 | $3,871.95 | $156.45 | — |
| STT | 8 | $185.86 | $185.25 | $1,482.04 | $-4.83 | $168.31 |
| VLO | 3 | $304.72 | $309.61 | $928.83 | $14.67 | $283.28 |
| WST | 3 | $336.32 | $356.71 | $1,070.13 | $61.17 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-765.33 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-10T14:38` entry buy **DOC** — momentum entry: rank 11, mom 0.312, vol 21%
- `2026-08-10T14:38` entry buy **HUM** — momentum entry: rank 3, mom 0.695, vol 39%
- `2026-08-07T20:10` system — eod_complete
- `2026-08-07T19:33` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T19:33` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T18:25` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T18:25` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T17:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T17:26` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T16:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T16:26` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T15:29` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T15:29` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T14:34` entry buy **CSCO** — momentum entry: rank 8, mom 0.353, vol 36%
- `2026-08-07T14:34` entry buy **BAX** — momentum entry: rank 4, mom 0.473, vol 50%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
