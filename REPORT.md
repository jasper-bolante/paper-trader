# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-22 20:40 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,785.37** |
| Total return since inception | -1.07% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,148.03 (0.74%) |
| Positions value | $18,401.44 |
| Settled cash | $1,375.71 |
| Unsettled cash (T+1) | $13.89 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.14% | 0.56% |
| Annualized volatility | 9.37% | 10.55% |
| Sharpe (rf 4%) | -3.47 | 1.01 |
| Max drawdown | 1.77% | 1.73% |
| EOD observations | 11 | 11 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $65.86 | $856.18 | $-14.06 | $61.84 |
| DDOG | 3 | $260.67 | $245.65 | $736.95 | $-45.05 | $236.93 |
| DVA | 6 | $227.39 | $232.06 | $1,392.36 | $28.00 | $213.53 |
| FFIV | 3 | $430.59 | $400.47 | $1,201.41 | $-90.36 | $388.22 |
| FTNT | 5 | $155.14 | $154.98 | $774.90 | $-0.78 | $150.16 |
| HUM | 2 | $401.64 | $397.54 | $795.08 | $-8.20 | $366.83 |
| IBKR | 10 | $95.61 | $93.44 | $934.45 | $-21.61 | $87.64 |
| MPC | 3 | $306.56 | $315.75 | $947.25 | $27.57 | $287.83 |
| NTAP | 5 | $161.48 | $166.53 | $832.67 | $25.29 | $149.88 |
| PSX | 5 | $215.50 | $211.35 | $1,056.77 | $-20.71 | $191.32 |
| SPY | 5 | $743.10 | $748.60 | $3,743.00 | $27.50 | — |
| STT | 8 | $185.86 | $185.24 | $1,481.92 | $-4.95 | $168.04 |
| TRGP | 5 | $282.92 | $284.38 | $1,421.90 | $7.29 | $255.94 |
| UNH | 3 | $425.21 | $431.32 | $1,293.96 | $18.34 | $393.25 |
| VLO | 3 | $304.72 | $310.88 | $932.62 | $18.47 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-22T20:40` system — corporate_actions_synced
- `2026-07-22T18:43` no_trade — no signals crossed action thresholds this hour
- `2026-07-22T18:43` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-07-22T16:57` no_trade — no signals crossed action thresholds this hour
- `2026-07-22T16:57` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-07-22T15:21` entry buy **PSX** — momentum entry: rank 14, mom 0.336, vol 34%
- `2026-07-22T15:21` entry buy **TRGP** — momentum entry: rank 10, mom 0.382, vol 28%
- `2026-07-22T15:21` no_trade skip_entry **WST** — sector cap: Health Care would exceed 25% of equity
- `2026-07-22T15:21` no_trade skip_entry **CVS** — sector cap: Health Care would exceed 25% of equity
- `2026-07-21T20:46` system — eod_complete
- `2026-07-21T18:51` no_trade — no signals crossed action thresholds this hour
- `2026-07-21T18:51` no_trade skip_entry **DOC** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **CSX** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **MGM** — insufficient investable cash (size $483, need >= $500)
- `2026-07-21T18:51` no_trade skip_entry **PSX** — insufficient investable cash (size $483, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
