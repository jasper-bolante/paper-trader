# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-11 17:31 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,658.60** |
| Total return since inception | -1.71% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,799.89 (4.00%) |
| Positions value | $17,862.33 |
| Settled cash | $1,043.31 |
| Unsettled cash (T+1) | $759.75 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.78% | 3.82% |
| Annualized volatility | 13.07% | 14.44% |
| Sharpe (rf 4%) | -1.75 | 2.64 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 24 | 24 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.68 | $775.18 | $11.57 | $25.00 |
| BBY | 14 | $88.05 | $83.22 | $1,165.08 | $-67.67 | $79.24 |
| CSCO | 8 | $131.57 | $120.72 | $965.76 | $-86.83 | $110.34 |
| CSX | 17 | $50.29 | $50.20 | $853.40 | $-1.55 | $46.01 |
| DOC | 40 | $21.90 | $20.75 | $829.80 | $-46.27 | $18.97 |
| FTNT | 7 | $149.43 | $162.88 | $1,140.16 | $94.12 | $151.44 |
| HPQ | 31 | $28.20 | $29.05 | $900.55 | $26.31 | $27.04 |
| HUM | 2 | $398.00 | $375.25 | $750.50 | $-45.49 | $348.07 |
| MPC | 3 | $306.56 | $332.99 | $998.97 | $79.29 | $288.24 |
| NTAP | 5 | $161.48 | $197.89 | $989.45 | $182.07 | $178.85 |
| PSX | 5 | $215.50 | $222.50 | $1,112.53 | $35.05 | $193.81 |
| SPY | 5 | $743.10 | $770.80 | $3,854.00 | $138.50 | — |
| STT | 8 | $185.86 | $187.96 | $1,503.64 | $16.77 | $168.31 |
| VLO | 3 | $304.72 | $322.38 | $967.14 | $52.98 | $283.47 |
| WST | 3 | $336.32 | $352.06 | $1,056.18 | $47.22 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-11T17:31` no_trade — no signals crossed action thresholds this hour
- `2026-08-11T17:31` no_trade skip_entry **TGT** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **URI** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **NUE** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **GEN** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **UAL** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **CNC** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **DAL** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **FFIV** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade — no signals crossed action thresholds this hour
- `2026-08-11T16:27` no_trade skip_entry **TGT** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **URI** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **NUE** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **GEN** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T16:27` no_trade skip_entry **UAL** — insufficient investable cash (size $54, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
