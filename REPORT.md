# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-15 21:41 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,717.61** |
| Total return since inception | -1.41% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,391.87 (1.96%) |
| Positions value | $18,633.61 |
| Settled cash | $1,083.84 |
| Unsettled cash (T+1) | $12.06 |
| Tax reserve | $11.90 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.48% | 1.78% |
| Annualized volatility | 11.24% | 11.67% |
| Sharpe (rf 4%) | -1.00 | 0.51 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 49 | 49 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $192.78 | $771.10 | $3.98 | $173.50 |
| BBY | 8 | $101.21 | $93.22 | $745.76 | $-63.92 | $83.90 |
| FDS | 3 | $293.49 | $277.07 | $831.21 | $-49.25 | $253.30 |
| GPC | 8 | $132.94 | $130.79 | $1,046.36 | $-17.17 | $119.77 |
| HUM | 2 | $426.49 | $396.60 | $793.20 | $-59.77 | $371.57 |
| INCY | 6 | $122.55 | $121.73 | $730.38 | $-4.89 | $110.18 |
| IQV | 2 | $255.46 | $269.65 | $539.30 | $28.39 | $244.26 |
| MPC | 3 | $306.56 | $410.62 | $1,231.86 | $312.18 | $369.56 |
| NTAP | 5 | $206.27 | $189.85 | $949.25 | $-82.10 | $179.40 |
| PSX | 5 | $215.50 | $264.97 | $1,324.85 | $247.37 | $238.47 |
| RVTY | 9 | $122.75 | $140.17 | $1,261.53 | $156.81 | $126.15 |
| SPY | 5 | $743.10 | $757.66 | $3,788.30 | $72.80 | — |
| STT | 8 | $185.86 | $185.12 | $1,480.92 | $-5.95 | $174.87 |
| TECH | 12 | $72.32 | $72.33 | $867.96 | $0.12 | $65.20 |
| TGT | 7 | $162.82 | $154.32 | $1,080.24 | $-59.47 | $147.91 |
| VLO | 3 | $304.72 | $397.13 | $1,191.39 | $277.23 | $357.42 |

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
