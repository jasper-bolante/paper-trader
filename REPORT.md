# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-19 19:26 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,204.15** |
| Total return since inception | 1.02% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,543.94 (2.72%) |
| Positions value | $18,017.33 |
| Settled cash | $1,486.55 |
| Unsettled cash (T+1) | $715.13 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.66% | 2.54% |
| Annualized volatility | 11.10% | 11.17% |
| Sharpe (rf 4%) | -0.10 | 0.49 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 72 | 72 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| APA | 19 | $44.15 | $49.66 | $943.45 | $104.56 | $44.24 |
| CRL | 3 | $296.67 | $300.38 | $901.15 | $11.13 | $279.86 |
| DDOG | 3 | $264.28 | $262.06 | $786.16 | $-6.69 | $222.33 |
| FFIV | 2 | $448.44 | $455.48 | $910.96 | $14.07 | $431.75 |
| IQV | 2 | $255.46 | $264.82 | $529.64 | $18.73 | $247.54 |
| MPC | 3 | $399.06 | $472.56 | $1,417.68 | $220.51 | $436.32 |
| NTAP | 4 | $214.92 | $206.60 | $826.42 | $-33.25 | $193.37 |
| PLTR | 5 | $194.57 | $194.53 | $972.67 | $-0.19 | $175.08 |
| PSX | 5 | $215.50 | $289.76 | $1,448.80 | $371.32 | $267.61 |
| RVTY | 9 | $122.75 | $152.25 | $1,370.20 | $265.48 | $141.67 |
| SPY | 5 | $743.10 | $768.33 | $3,841.65 | $126.15 | — |
| TECH | 12 | $72.32 | $72.48 | $869.82 | $1.98 | $65.36 |
| VLO | 3 | $392.61 | $432.83 | $1,298.49 | $120.67 | $413.91 |
| WST | 2 | $370.69 | $384.29 | $768.57 | $27.19 | $345.43 |
| ZBRA | 3 | $345.13 | $377.22 | $1,131.66 | $96.28 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,218.01 | $0.00 | $1,200.98 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-19T19:26` entry buy **PLTR** — momentum entry: rank 7, mom 0.620, vol 39%
- `2026-10-19T19:26` no_trade skip_entry **TMO** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **CNC** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **CRM** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **A** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **MSFT** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **NOW** — insufficient investable cash (size $461, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **HUM** — insufficient investable cash (size $867, need >= $500)
- `2026-10-19T19:26` no_trade skip_entry **VEEV** — sector cap: Health Care would exceed 25% of equity
- `2026-10-19T19:26` exit sell **META** — momentum rank decayed (None > 150 or ineligible: volatility 0.5053586052163451 above cap 0.5)
- `2026-10-16T21:36` system — eod_complete
- `2026-10-16T17:39` entry buy **DDOG** — momentum entry: rank 3, mom 0.788, vol 44%
- `2026-10-16T17:39` no_trade skip_entry **CRM** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **MSFT** — insufficient investable cash (size $384, need >= $500)
- `2026-10-16T17:39` no_trade skip_entry **NOW** — insufficient investable cash (size $384, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
