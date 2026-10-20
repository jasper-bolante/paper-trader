# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-20 21:48 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,340.97** |
| Total return since inception | 1.70% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,740.95 (3.70%) |
| Positions value | $19,213.63 |
| Settled cash | $1,130.16 |
| Unsettled cash (T+1) | $12.04 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.64% | 3.52% |
| Annualized volatility | 11.04% | 11.07% |
| Sharpe (rf 4%) | 0.20 | 0.77 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 74 | 74 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $49.89 | $947.91 | $109.02 | $44.90 |
| CRL | 3 | $296.67 | $315.45 | $946.35 | $56.33 | $283.90 |
| DDOG | 3 | $264.28 | $256.25 | $768.75 | $-24.10 | $234.24 |
| EL | 10 | $105.95 | $106.08 | $1,060.75 | $1.27 | $95.47 |
| FFIV | 2 | $448.44 | $457.23 | $914.46 | $17.57 | $431.75 |
| IQV | 2 | $255.46 | $267.60 | $535.19 | $24.28 | $247.54 |
| MPC | 3 | $399.06 | $474.76 | $1,424.28 | $227.11 | $436.32 |
| NTAP | 4 | $214.92 | $209.95 | $839.80 | $-19.87 | $193.37 |
| PLTR | 5 | $194.57 | $192.58 | $962.90 | $-9.96 | $175.08 |
| PSX | 5 | $215.50 | $291.08 | $1,455.40 | $377.92 | $267.61 |
| RVTY | 9 | $122.75 | $155.90 | $1,403.06 | $298.34 | $141.67 |
| SPY | 5 | $743.10 | $770.63 | $3,853.15 | $137.65 | — |
| TECH | 12 | $72.32 | $72.59 | $871.08 | $3.24 | $65.36 |
| VLO | 3 | $392.61 | $433.84 | $1,301.52 | $123.70 | $413.91 |
| WST | 2 | $370.69 | $388.82 | $777.64 | $36.26 | $349.94 |
| ZBRA | 3 | $345.13 | $383.80 | $1,151.40 | $116.02 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,218.01 | $0.00 | $1,200.98 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-20T21:48` system — corporate_actions_synced
- `2026-10-20T18:05` entry buy **EL** — momentum entry: rank 20, mom 0.290, vol 36%
- `2026-10-20T18:05` no_trade skip_entry **CRM** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **CNC** — sector cap: Health Care would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **MSFT** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **NOW** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **WDAY** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **HUM** — sector cap: Health Care would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **VEEV** — sector cap: Health Care would exceed 25% of equity
- `2026-10-20T18:05` no_trade skip_entry **FTNT** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-19T23:01` system — eod_complete
- `2026-10-19T23:01` system — corporate_actions_synced
- `2026-10-19T19:26` entry buy **PLTR** — momentum entry: rank 7, mom 0.620, vol 39%
- `2026-10-19T19:26` no_trade skip_entry **TMO** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **CNC** — insufficient investable cash (size $461, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
