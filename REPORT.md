# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-13 14:39 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,900.53** |
| Total return since inception | -0.50% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,791.55 (3.96%) |
| Positions value | $17,808.59 |
| Settled cash | $1,260.94 |
| Unsettled cash (T+1) | $837.97 |
| Tax reserve | $6.97 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.21% | 3.77% |
| Annualized volatility | 12.71% | 13.90% |
| Sharpe (rf 4%) | -1.22 | 2.47 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 26 | 26 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.04 | $757.12 | $-6.49 | $25.00 |
| BBY | 14 | $88.05 | $84.47 | $1,182.65 | $-50.10 | $79.24 |
| CSCO | 8 | $131.57 | $115.09 | $920.76 | $-131.83 | $110.34 |
| CSX | 17 | $50.29 | $50.57 | $859.69 | $4.74 | $46.01 |
| FTNT | 7 | $149.43 | $163.67 | $1,145.69 | $99.65 | $151.44 |
| HPQ | 31 | $28.20 | $30.27 | $938.52 | $64.28 | $27.04 |
| HUM | 2 | $398.00 | $383.83 | $767.66 | $-28.33 | $349.89 |
| MPC | 3 | $306.56 | $351.42 | $1,054.26 | $134.58 | $313.38 |
| NTAP | 5 | $161.48 | $206.81 | $1,034.05 | $226.67 | $181.81 |
| NUE | 2 | $269.82 | $271.62 | $543.24 | $3.60 | $244.43 |
| PSX | 5 | $215.50 | $227.90 | $1,139.50 | $62.02 | $202.98 |
| SPY | 5 | $743.10 | $778.91 | $3,894.55 | $179.05 | — |
| STT | 8 | $185.86 | $191.32 | $1,530.60 | $43.73 | $171.10 |
| VLO | 3 | $304.72 | $332.53 | $997.59 | $83.43 | $297.31 |
| WST | 3 | $336.32 | $347.57 | $1,042.71 | $33.75 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-857.70 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-13T14:39` no_trade skip_entry **EXPE** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **CPAY** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **GEN** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **XYZ** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **CRL** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **FFIV** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **URI** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` no_trade skip_entry **CNC** — insufficient investable cash (size $259, need >= $500)
- `2026-08-13T14:39` exit sell **DOC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-12T21:23` system — eod_complete
- `2026-08-12T21:23` system **NUE** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-12T21:23` system — corporate_actions_synced
- `2026-08-12T19:40` no_trade — no signals crossed action thresholds this hour
- `2026-08-12T19:40` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-12T18:29` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
