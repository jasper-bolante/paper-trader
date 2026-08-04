# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-04 15:58 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,666.39** |
| Total return since inception | -1.67% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,388.37 (1.94%) |
| Positions value | $18,292.38 |
| Settled cash | $1,376.55 |
| Unsettled cash (T+1) | $4.26 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.38% | 1.76% |
| Annualized volatility | 9.38% | 14.88% |
| Sharpe (rf 4%) | -3.97 | 1.45 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 19 | 19 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BBY | 14 | $88.05 | $85.11 | $1,191.54 | $-41.21 | $79.24 |
| CSX | 17 | $50.29 | $50.43 | $857.31 | $2.36 | $45.34 |
| DDOG | 3 | $260.67 | $285.32 | $855.96 | $73.96 | $246.19 |
| DOC | 32 | $22.25 | $21.51 | $688.32 | $-23.70 | $20.55 |
| DVA | 6 | $227.39 | $231.18 | $1,387.05 | $22.69 | $216.78 |
| FTNT | 7 | $149.43 | $165.91 | $1,161.37 | $115.33 | $146.83 |
| HUM | 2 | $383.80 | $363.88 | $727.76 | $-39.83 | $327.49 |
| MPC | 3 | $306.56 | $310.26 | $930.78 | $11.10 | $287.83 |
| NTAP | 5 | $161.48 | $191.48 | $957.40 | $150.02 | $164.66 |
| PSX | 5 | $215.50 | $204.00 | $1,020.00 | $-57.48 | $191.32 |
| SPY | 5 | $743.10 | $768.54 | $3,842.70 | $127.20 | — |
| STT | 8 | $185.86 | $186.51 | $1,492.08 | $5.21 | $168.04 |
| UNH | 3 | $425.21 | $408.76 | $1,226.30 | $-49.32 | $393.25 |
| VLO | 3 | $304.72 | $305.86 | $917.58 | $3.42 | $283.28 |
| WST | 3 | $336.32 | $345.41 | $1,036.23 | $27.27 | $313.25 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-699.17 | $0.00 | $134.95 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-04T15:58` entry buy **HUM** — momentum entry: rank 5, mom 0.601, vol 37%
- `2026-08-04T15:58` no_trade skip_entry **WELL** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **VTRS** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **ALL** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **CVS** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **TRV** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **HPQ** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **FFIV** — insufficient investable cash (size $385, need >= $500)
- `2026-08-04T15:58` no_trade skip_entry **CNC** — insufficient investable cash (size $385, need >= $500)
- `2026-08-03T20:14` system — eod_complete
- `2026-08-03T20:14` system — corporate_actions_synced
- `2026-08-03T18:18` no_trade — no signals crossed action thresholds this hour
- `2026-08-03T18:18` no_trade skip_entry **ALL** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T18:18` no_trade skip_entry **NUE** — insufficient investable cash (size $5, need >= $500)
- `2026-08-03T18:18` no_trade skip_entry **HPQ** — insufficient investable cash (size $5, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
