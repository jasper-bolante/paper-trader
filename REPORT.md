# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-17 14:03 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,901.01** |
| Total return since inception | -0.49% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,886.29 (4.43%) |
| Positions value | $17,874.47 |
| Settled cash | $1,119.18 |
| Unsettled cash (T+1) | $914.34 |
| Tax reserve | $6.97 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.50% | 4.25% |
| Annualized volatility | 12.72% | 13.52% |
| Sharpe (rf 4%) | -0.62 | 2.64 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 28 | 28 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.24 | $734.72 | $-28.89 | $25.00 |
| BBY | 14 | $88.05 | $86.60 | $1,212.40 | $-20.35 | $79.24 |
| CNC | 8 | $75.27 | $65.26 | $522.08 | $-80.05 | $58.73 |
| CRL | 2 | $285.12 | $284.96 | $569.93 | $-0.31 | $256.47 |
| CSX | 17 | $50.29 | $50.66 | $861.13 | $6.18 | $46.01 |
| FTNT | 7 | $149.43 | $156.84 | $1,097.88 | $51.84 | $151.44 |
| HUM | 2 | $398.00 | $383.19 | $766.38 | $-29.61 | $350.32 |
| MPC | 3 | $306.56 | $361.57 | $1,084.71 | $165.03 | $321.00 |
| NTAP | 5 | $161.48 | $204.63 | $1,023.15 | $215.77 | $186.39 |
| NUE | 2 | $269.82 | $268.92 | $537.84 | $-1.80 | $245.24 |
| PANW | 2 | $388.28 | $376.98 | $753.95 | $-22.61 | $349.27 |
| PSX | 5 | $215.50 | $238.06 | $1,190.30 | $112.82 | $210.25 |
| SPY | 5 | $743.10 | $775.04 | $3,875.20 | $159.70 | — |
| STT | 8 | $185.86 | $193.84 | $1,550.76 | $63.89 | $172.62 |
| VLO | 3 | $304.72 | $347.34 | $1,042.02 | $127.86 | $308.51 |
| WST | 3 | $336.32 | $350.67 | $1,052.01 | $43.05 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-17T14:03` entry buy **CNC** — momentum entry: rank 5, mom 0.422, vol 38%
- `2026-08-17T14:03` entry buy **CRL** — momentum entry: rank 4, mom 0.464, vol 47%
- `2026-08-17T14:03` exit sell **HPQ** — momentum rank decayed (None > 150 or ineligible: volatility 0.5054050659101534 above cap 0.5)
- `2026-08-14T20:05` system — eod_complete
- `2026-08-14T19:30` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T19:30` no_trade skip_entry **URI** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **TRV** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **ALL** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **CPAY** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **GEN** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **FFIV** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **CNC** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T19:30` no_trade skip_entry **CRL** — insufficient investable cash (size $318, need >= $500)
- `2026-08-14T18:27` no_trade — no signals crossed action thresholds this hour
- `2026-08-14T18:27` no_trade skip_entry **URI** — insufficient investable cash (size $317, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
