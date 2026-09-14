# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-14 22:42 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,580.03** |
| Total return since inception | -2.10% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,475.17 (2.38%) |
| Positions value | $16,983.28 |
| Settled cash | $1,112.22 |
| Unsettled cash (T+1) | $1,496.43 |
| Tax reserve | $11.90 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.17% | 2.20% |
| Annualized volatility | 11.23% | 11.74% |
| Sharpe (rf 4%) | -1.35 | 0.71 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 48 | 48 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| FDS | 3 | $293.49 | $277.33 | $831.99 | $-48.47 | $253.30 |
| GPC | 8 | $132.94 | $133.08 | $1,064.64 | $1.11 | $119.77 |
| HUM | 2 | $426.49 | $407.64 | $815.28 | $-37.69 | $371.57 |
| INCY | 6 | $122.55 | $122.14 | $732.84 | $-2.43 | $110.18 |
| IQV | 2 | $255.46 | $265.57 | $531.14 | $20.23 | $244.26 |
| MPC | 3 | $306.56 | $396.46 | $1,189.38 | $269.70 | $359.56 |
| NTAP | 5 | $206.27 | $188.22 | $941.10 | $-90.25 | $179.40 |
| PSX | 5 | $215.50 | $256.84 | $1,284.20 | $206.72 | $234.77 |
| RVTY | 9 | $122.75 | $128.53 | $1,156.77 | $52.05 | $115.68 |
| SPY | 5 | $743.10 | $760.75 | $3,803.78 | $88.28 | — |
| STT | 8 | $185.86 | $188.16 | $1,505.28 | $18.41 | $174.87 |
| TECH | 12 | $72.32 | $72.29 | $867.48 | $-0.36 | $65.20 |
| TGT | 7 | $162.82 | $158.72 | $1,111.04 | $-28.67 | $147.91 |
| VLO | 3 | $304.72 | $382.79 | $1,148.37 | $234.21 | $351.48 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,170.24 | $0.00 | $957.59 |

Dividends received: $79.33. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-14T22:42` system **GPC** — cash settles on pay date; 15% dividend tax reserved
- `2026-09-14T22:42` system — corporate_actions_synced
- `2026-09-14T18:50` entry buy **GPC** — momentum entry: rank 14, mom 0.285, vol 23%
- `2026-09-14T18:50` no_trade skip_entry **ANET** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **BNY** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **MET** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **BBY** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **GEN** — insufficient investable cash (size $123, need >= $500)
- `2026-09-14T18:50` no_trade skip_entry **MRK** — sector cap: Health Care would exceed 25% of equity
- `2026-09-14T18:50` no_trade skip_entry **CNC** — sector cap: Health Care would exceed 25% of equity
- `2026-09-14T18:50` no_trade skip_entry **CRL** — sector cap: Health Care would exceed 25% of equity
- `2026-09-14T18:50` exit sell **PAYX** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-14T18:49` exit sell **CRL** — trailing stop 10%
- `2026-09-11T22:44` system — eod_complete
- `2026-09-11T19:58` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
