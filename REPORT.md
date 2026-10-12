# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-12 21:49 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,535.46** |
| Total return since inception | 2.68% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,938.23 (4.69%) |
| Positions value | $18,801.83 |
| Settled cash | $1,736.45 |
| Unsettled cash (T+1) | $12.04 |
| Tax reserve | $14.86 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 2.61% | 4.51% |
| Annualized volatility | 10.85% | 11.01% |
| Sharpe (rf 4%) | 0.58 | 1.20 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 68 | 68 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| AMD | 1 | $650.00 | $594.19 | $594.19 | $-55.81 | $581.31 |
| ANET | 4 | $191.78 | $210.85 | $843.40 | $76.28 | $195.06 |
| APA | 19 | $44.15 | $46.85 | $890.24 | $51.35 | $42.17 |
| CRL | 3 | $296.67 | $302.20 | $906.60 | $16.58 | $279.86 |
| FFIV | 2 | $448.44 | $473.42 | $946.84 | $49.95 | $431.75 |
| IQV | 2 | $255.46 | $262.25 | $524.51 | $13.60 | $247.54 |
| META | 1 | $723.49 | $743.02 | $743.02 | $19.53 | $668.72 |
| MPC | 3 | $399.06 | $459.48 | $1,378.43 | $181.26 | $417.31 |
| NTAP | 5 | $206.27 | $239.22 | $1,196.08 | $164.73 | $215.29 |
| PSX | 5 | $215.50 | $281.80 | $1,408.98 | $331.50 | $253.62 |
| RVTY | 9 | $122.75 | $155.71 | $1,401.39 | $296.67 | $141.67 |
| SPY | 5 | $743.10 | $777.96 | $3,889.80 | $174.30 | — |
| TECH | 12 | $72.32 | $72.57 | $870.84 | $3.00 | $65.36 |
| VLO | 3 | $392.61 | $436.20 | $1,308.62 | $130.80 | $399.71 |
| WST | 2 | $370.69 | $367.33 | $734.66 | $-6.72 | $339.09 |
| ZBRA | 3 | $345.13 | $388.08 | $1,164.24 | $128.86 | $349.27 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,124.61 | $0.00 | $1,142.35 |

Dividends received: $99.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-09T23:25` system — eod_complete
- `2026-10-09T23:25` system — corporate_actions_synced
- `2026-10-09T18:57` no_trade — no signals crossed action thresholds this hour
- `2026-10-09T18:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-09T18:57` system **NTAP** — cash settles on pay date; 15% dividend tax reserved
- `2026-10-08T23:52` system — eod_complete
- `2026-10-08T19:23` no_trade — no signals crossed action thresholds this hour
- `2026-10-08T19:23` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-07T23:43` system — eod_complete
- `2026-10-07T19:28` entry buy **META** — momentum entry: rank 20, mom 0.344, vol 47%
- `2026-10-07T19:28` entry buy **AMD** — momentum entry: rank 2, mom 1.073, vol 49%
- `2026-10-07T19:28` no_trade skip_entry **TMO** — sector cap: Health Care would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **MSFT** — sector cap: Information Technology would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **A** — sector cap: Health Care would exceed 25% of equity
- `2026-10-07T19:28` no_trade skip_entry **PLTR** — sector cap: Information Technology would exceed 25% of equity

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
