# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-19 19:51 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,699.45** |
| Total return since inception | -1.50% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,652.67 (3.26%) |
| Positions value | $17,074.70 |
| Settled cash | $1,366.98 |
| Unsettled cash (T+1) | $1,266.14 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.75% | 3.08% |
| Annualized volatility | 12.31% | 13.37% |
| Sharpe (rf 4%) | -0.80 | 1.74 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 30 | 30 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.57 | $743.82 | $-19.79 | $25.00 |
| BBY | 14 | $88.05 | $89.02 | $1,246.28 | $13.53 | $79.24 |
| CNC | 8 | $75.27 | $64.66 | $517.28 | $-84.85 | $58.73 |
| CRL | 2 | $285.12 | $289.66 | $579.32 | $9.08 | $258.00 |
| CSX | 17 | $50.29 | $50.76 | $862.84 | $7.88 | $46.01 |
| EXPE | 2 | $331.47 | $327.01 | $654.02 | $-8.92 | $298.17 |
| FTNT | 7 | $149.43 | $152.57 | $1,067.99 | $21.95 | $151.44 |
| MPC | 3 | $306.56 | $360.25 | $1,080.75 | $161.07 | $330.10 |
| NTAP | 5 | $161.48 | $194.32 | $971.60 | $164.22 | $186.39 |
| PANW | 2 | $388.28 | $358.07 | $716.15 | $-60.41 | $349.27 |
| PSX | 5 | $215.50 | $241.57 | $1,207.88 | $130.39 | $219.13 |
| SPY | 5 | $743.10 | $768.49 | $3,842.45 | $126.95 | — |
| STT | 8 | $185.86 | $185.69 | $1,485.52 | $-1.35 | $173.64 |
| VLO | 3 | $304.72 | $345.60 | $1,036.79 | $122.63 | $315.01 |
| WST | 3 | $336.32 | $354.01 | $1,062.03 | $53.07 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-983.43 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-19T19:03` no_trade skip_entry **TECH** — insufficient investable cash (size $372, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
