# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-12 21:23 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,771.03** |
| Total return since inception | -1.14% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,791.55 (3.96%) |
| Positions value | $18,513.46 |
| Settled cash | $1,260.94 |
| Unsettled cash (T+1) | $3.60 |
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
| BAX | 28 | $27.27 | $26.95 | $754.60 | $-9.01 | $25.00 |
| BBY | 14 | $88.05 | $83.02 | $1,162.28 | $-70.47 | $79.24 |
| CSCO | 8 | $131.57 | $119.05 | $952.40 | $-100.19 | $110.34 |
| CSX | 17 | $50.29 | $50.09 | $851.53 | $-3.42 | $46.01 |
| DOC | 40 | $21.90 | $20.65 | $826.00 | $-50.07 | $18.97 |
| FTNT | 7 | $149.43 | $160.77 | $1,125.39 | $79.35 | $151.44 |
| HPQ | 31 | $28.20 | $29.27 | $907.22 | $32.98 | $27.04 |
| HUM | 2 | $398.00 | $388.77 | $777.54 | $-18.45 | $349.89 |
| MPC | 3 | $306.56 | $348.19 | $1,044.59 | $124.91 | $313.38 |
| NTAP | 5 | $161.48 | $202.01 | $1,010.05 | $202.67 | $181.81 |
| NUE | 2 | $269.82 | $271.58 | $543.17 | $3.53 | $244.43 |
| PSX | 5 | $215.50 | $225.53 | $1,127.65 | $50.17 | $202.98 |
| SPY | 5 | $743.10 | $772.51 | $3,862.55 | $147.05 | — |
| STT | 8 | $185.86 | $190.11 | $1,520.88 | $34.01 | $171.10 |
| VLO | 3 | $304.72 | $330.34 | $991.02 | $76.86 | $297.31 |
| WST | 3 | $336.32 | $352.20 | $1,056.60 | $47.64 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $46.46. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-12T21:23` system **NUE** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-12T21:23` system — corporate_actions_synced
- `2026-08-12T19:40` no_trade — no signals crossed action thresholds this hour
- `2026-08-12T19:40` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-12T18:29` no_trade — no signals crossed action thresholds this hour
- `2026-08-12T18:29` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-12T17:32` no_trade — no signals crossed action thresholds this hour
- `2026-08-12T17:32` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-12T16:28` no_trade — no signals crossed action thresholds this hour
- `2026-08-12T16:28` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-12T14:38` entry buy **NUE** — momentum entry: rank 9, mom 0.364, vol 34%
- `2026-08-11T21:24` system — eod_complete
- `2026-08-11T21:24` system — corporate_actions_synced
- `2026-08-11T19:38` no_trade — no signals crossed action thresholds this hour
- `2026-08-11T19:38` no_trade skip_entry **TGT** — insufficient investable cash (size $53, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
