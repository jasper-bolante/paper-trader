# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-27 18:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,530.05** |
| Total return since inception | 2.65% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,595.48 (2.98%) |
| Positions value | $18,192.28 |
| Settled cash | $1,094.93 |
| Unsettled cash (T+1) | $1,258.50 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 3.56% | 2.80% |
| Annualized volatility | 11.28% | 11.13% |
| Sharpe (rf 4%) | 0.72 | 0.51 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 78 | 78 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $50.67 | $962.73 | $123.84 | $46.71 |
| CRL | 3 | $296.67 | $356.61 | $1,069.83 | $179.81 | $321.62 |
| EL | 10 | $105.95 | $108.20 | $1,082.00 | $22.52 | $97.97 |
| FFIV | 2 | $448.44 | $457.97 | $915.94 | $19.05 | $431.75 |
| FTNT | 5 | $183.53 | $185.41 | $927.02 | $9.37 | $165.00 |
| IQV | 2 | $255.46 | $272.78 | $545.56 | $34.65 | $251.42 |
| MPC | 3 | $399.06 | $439.58 | $1,318.74 | $121.57 | $436.32 |
| NTAP | 4 | $214.92 | $229.31 | $917.24 | $57.57 | $199.86 |
| PLTR | 5 | $194.57 | $199.69 | $998.42 | $25.56 | $181.53 |
| PSX | 5 | $215.50 | $269.76 | $1,348.80 | $271.32 | $267.61 |
| RVTY | 9 | $122.75 | $161.75 | $1,455.75 | $351.03 | $144.30 |
| SPY | 5 | $743.10 | $769.25 | $3,846.25 | $130.75 | — |
| TECH | 12 | $72.32 | $72.64 | $871.62 | $3.78 | $65.43 |
| WST | 2 | $370.69 | $395.24 | $790.48 | $49.10 | $355.20 |
| ZBRA | 3 | $345.13 | $380.63 | $1,141.89 | $106.51 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,065.16 | $0.00 | $1,257.19 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-27T18:52` no_trade skip_entry **HPQ** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **CNC** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **IT** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **NOW** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **WDAY** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **HUM** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **VLO** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` no_trade skip_entry **VEEV** — insufficient investable cash (size $53, need >= $500)
- `2026-10-27T18:52` exit sell **VLO** — trailing stop 10%
- `2026-10-26T23:16` system — eod_complete
- `2026-10-26T19:30` no_trade — no signals crossed action thresholds this hour
- `2026-10-26T19:30` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-23T21:35` system — eod_complete
- `2026-10-23T17:57` no_trade — no signals crossed action thresholds this hour
- `2026-10-23T17:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
