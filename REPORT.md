# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-26 23:16 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,726.58** |
| Total return since inception | 3.63% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,595.48 (2.98%) |
| Positions value | $19,629.90 |
| Settled cash | $1,094.93 |
| Unsettled cash (T+1) | $17.42 |
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
| APA | 19 | $44.15 | $51.66 | $981.54 | $142.65 | $46.71 |
| CRL | 3 | $296.67 | $357.35 | $1,072.05 | $182.03 | $321.62 |
| EL | 10 | $105.95 | $108.85 | $1,088.50 | $29.02 | $97.97 |
| FFIV | 2 | $448.44 | $461.72 | $923.44 | $26.55 | $431.75 |
| FTNT | 5 | $183.53 | $183.33 | $916.65 | $-1.01 | $165.00 |
| IQV | 2 | $255.46 | $273.96 | $547.92 | $37.01 | $251.42 |
| MPC | 3 | $399.06 | $470.65 | $1,411.95 | $214.78 | $436.32 |
| NTAP | 4 | $214.92 | $222.07 | $888.28 | $28.61 | $199.86 |
| PLTR | 5 | $194.57 | $198.86 | $994.30 | $21.44 | $181.53 |
| PSX | 5 | $215.50 | $288.73 | $1,443.65 | $366.17 | $267.61 |
| RVTY | 9 | $122.75 | $160.34 | $1,443.02 | $338.30 | $144.30 |
| SPY | 5 | $743.10 | $765.23 | $3,826.12 | $110.62 | — |
| TECH | 12 | $72.32 | $72.70 | $872.40 | $4.56 | $65.43 |
| VLO | 3 | $392.61 | $426.38 | $1,279.12 | $101.31 | $413.91 |
| WST | 2 | $370.69 | $394.67 | $789.34 | $47.96 | $355.20 |
| ZBRA | 3 | $345.13 | $383.87 | $1,151.61 | $116.23 | $352.09 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,128.42 | $0.00 | $1,257.19 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-26T19:30` no_trade — no signals crossed action thresholds this hour
- `2026-10-26T19:30` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-23T21:35` system — eod_complete
- `2026-10-23T17:57` no_trade — no signals crossed action thresholds this hour
- `2026-10-23T17:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-23T17:56` system **RVTY** — cash settles on pay date; 15% dividend tax reserved
- `2026-10-22T21:52` system — eod_complete
- `2026-10-22T18:08` entry buy **FTNT** — momentum entry: rank 4, mom 0.728, vol 43%
- `2026-10-22T18:07` system **APA** — cash settles on pay date; 15% dividend tax reserved
- `2026-10-21T21:55` system — eod_complete
- `2026-10-21T18:12` no_trade skip_entry **IT** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **CRM** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **CNC** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **WDAY** — insufficient investable cash (size $87, need >= $500)
- `2026-10-21T18:12` no_trade skip_entry **NOW** — insufficient investable cash (size $87, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
