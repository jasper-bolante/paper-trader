# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-19 20:56 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,714.04** |
| Total return since inception | -1.43% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,700.58 (3.50%) |
| Positions value | $17,089.29 |
| Settled cash | $1,366.98 |
| Unsettled cash (T+1) | $1,266.14 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.50% | 3.32% |
| Annualized volatility | 12.28% | 13.14% |
| Sharpe (rf 4%) | -1.30 | 1.85 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 31 | 31 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.67 | $746.76 | $-16.85 | $25.00 |
| BBY | 14 | $88.05 | $89.25 | $1,249.50 | $16.75 | $80.33 |
| CNC | 8 | $75.27 | $64.72 | $517.76 | $-84.37 | $58.73 |
| CRL | 2 | $285.12 | $289.98 | $579.96 | $9.72 | $260.98 |
| CSX | 17 | $50.29 | $50.68 | $861.56 | $6.61 | $46.01 |
| EXPE | 2 | $331.47 | $326.29 | $652.58 | $-10.36 | $298.17 |
| FTNT | 7 | $149.43 | $152.82 | $1,069.74 | $23.70 | $151.44 |
| MPC | 3 | $306.56 | $360.78 | $1,082.34 | $162.66 | $330.10 |
| NTAP | 5 | $161.48 | $194.49 | $972.45 | $165.07 | $186.39 |
| PANW | 2 | $388.28 | $359.76 | $719.52 | $-57.04 | $349.27 |
| PSX | 5 | $215.50 | $242.19 | $1,210.97 | $133.49 | $219.13 |
| SPY | 5 | $743.10 | $769.13 | $3,845.65 | $130.15 | — |
| STT | 8 | $185.86 | $185.72 | $1,485.76 | $-1.11 | $173.64 |
| VLO | 3 | $304.72 | $345.95 | $1,037.87 | $123.71 | $315.01 |
| WST | 3 | $336.32 | $352.29 | $1,056.87 | $47.91 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-983.43 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-19T20:56` system — corporate_actions_synced
- `2026-08-19T19:51` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T19:51` no_trade skip_entry **WSM** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **NUE** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **APA** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **TGT** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **BKNG** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **TECH** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **IQV** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:51` no_trade skip_entry **VEEV** — insufficient investable cash (size $374, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **WSM** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **NUE** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **APA** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **TGT** — insufficient investable cash (size $372, need >= $500)
- `2026-08-19T19:03` no_trade skip_entry **BKNG** — insufficient investable cash (size $372, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
