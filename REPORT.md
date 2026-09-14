# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-14 18:50 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,554.52** |
| Total return since inception | -2.23% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,568.43 (2.84%) |
| Positions value | $16,964.99 |
| Settled cash | $1,112.22 |
| Unsettled cash (T+1) | $1,487.93 |
| Tax reserve | $10.62 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.05% | 2.66% |
| Annualized volatility | 11.35% | 11.81% |
| Sharpe (rf 4%) | -1.30 | 0.94 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 47 | 47 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| FDS | 3 | $293.49 | $273.65 | $820.95 | $-59.51 | $253.30 |
| GPC | 8 | $132.94 | $132.87 | $1,062.96 | $-0.57 | $119.58 |
| HUM | 2 | $426.49 | $415.14 | $830.28 | $-22.69 | $371.57 |
| INCY | 6 | $122.55 | $122.52 | $735.12 | $-0.15 | $110.18 |
| IQV | 2 | $255.46 | $264.52 | $529.05 | $18.14 | $244.26 |
| MPC | 3 | $306.56 | $392.04 | $1,176.11 | $256.43 | $359.56 |
| NTAP | 5 | $206.27 | $192.07 | $960.38 | $-70.97 | $179.40 |
| PSX | 5 | $215.50 | $255.45 | $1,277.25 | $199.77 | $234.77 |
| RVTY | 9 | $122.75 | $125.95 | $1,133.55 | $28.83 | $111.97 |
| SPY | 5 | $743.10 | $762.50 | $3,812.50 | $97.00 | — |
| STT | 8 | $185.86 | $187.94 | $1,503.48 | $16.61 | $174.87 |
| TECH | 12 | $72.32 | $72.19 | $866.34 | $-1.50 | $65.20 |
| TGT | 7 | $162.82 | $159.40 | $1,115.80 | $-23.91 | $147.91 |
| VLO | 3 | $304.72 | $380.41 | $1,141.23 | $227.07 | $351.48 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,170.24 | $0.00 | $957.59 |

Dividends received: $70.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-09-11T19:58` no_trade skip_entry **NUE** — insufficient investable cash (size $53, need >= $500)
- `2026-09-11T19:58` no_trade skip_entry **CF** — insufficient investable cash (size $53, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
