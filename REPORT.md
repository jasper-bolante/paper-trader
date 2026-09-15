# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-15 17:44 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,717.65** |
| Total return since inception | -1.41% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,475.17 (2.38%) |
| Positions value | $18,633.65 |
| Settled cash | $1,083.84 |
| Unsettled cash (T+1) | $12.06 |
| Tax reserve | $11.90 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.17% | 2.20% |
| Annualized volatility | 11.23% | 11.74% |
| Sharpe (rf 4%) | -1.35 | 0.71 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 48 | 48 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $191.68 | $766.72 | $-0.40 | $172.51 |
| BBY | 8 | $101.21 | $93.22 | $745.80 | $-63.88 | $83.90 |
| FDS | 3 | $293.49 | $279.80 | $839.40 | $-41.06 | $253.30 |
| GPC | 8 | $132.94 | $131.21 | $1,049.68 | $-13.85 | $119.77 |
| HUM | 2 | $426.49 | $396.24 | $792.48 | $-60.49 | $371.57 |
| INCY | 6 | $122.55 | $121.17 | $726.99 | $-8.28 | $110.18 |
| IQV | 2 | $255.46 | $269.92 | $539.84 | $28.93 | $244.26 |
| MPC | 3 | $306.56 | $411.96 | $1,235.88 | $316.20 | $359.56 |
| NTAP | 5 | $206.27 | $190.67 | $953.35 | $-78.00 | $179.40 |
| PSX | 5 | $215.50 | $266.15 | $1,330.75 | $253.27 | $234.77 |
| RVTY | 9 | $122.75 | $138.43 | $1,245.83 | $141.11 | $115.68 |
| SPY | 5 | $743.10 | $757.17 | $3,785.88 | $70.38 | — |
| STT | 8 | $185.86 | $184.59 | $1,476.72 | $-10.15 | $174.87 |
| TECH | 12 | $72.32 | $72.25 | $866.94 | $-0.90 | $65.20 |
| TGT | 7 | $162.82 | $155.20 | $1,086.40 | $-53.31 | $147.91 |
| VLO | 3 | $304.72 | $397.00 | $1,191.00 | $276.84 | $351.48 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,106.19 | $0.00 | $1,021.65 |

Dividends received: $79.33. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-15T17:44` entry buy **BBY** — momentum entry: rank 13, mom 0.308, vol 41%
- `2026-09-15T17:44` entry buy **ANET** — momentum entry: rank 11, mom 0.357, vol 49%
- `2026-09-15T17:44` no_trade skip_entry **CRL** — sector cap: Health Care would exceed 25% of equity
- `2026-09-14T22:42` system — eod_complete
- `2026-09-14T22:42` system **GPC** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-14T22:42` system — corporate_actions_synced
- `2026-09-14T18:50` entry buy **GPC** — momentum entry: rank 14, mom 0.285, vol 23%
- `2026-09-14T18:50` no_trade skip_entry **ANET** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **BNY** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **MET** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **BBY** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **GEN** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **MRK** — sector cap: Health Care would exceed 25% of equity
- `2026-09-14T18:50` no_trade skip_entry **CNC** — sector cap: Health Care would exceed 25% of equity
- `2026-09-14T18:50` no_trade skip_entry **CRL** — sector cap: Health Care would exceed 25% of equity

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
