# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-09-24 21:43 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,637.35** |
| Total return since inception | -1.81% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,651.06 (3.26%) |
| Positions value | $16,654.51 |
| Settled cash | $2,971.41 |
| Unsettled cash (T+1) | $25.90 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.88% | 3.07% |
| Annualized volatility | 11.34% | 11.67% |
| Sharpe (rf 4%) | -1.06 | 0.90 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 56 | 56 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $205.71 | $822.84 | $55.72 | $185.14 |
| APA | 19 | $44.15 | $43.68 | $829.92 | $-8.97 | $39.73 |
| BBY | 8 | $101.21 | $90.95 | $727.60 | $-82.08 | $85.36 |
| CRL | 3 | $296.67 | $294.48 | $883.43 | $-6.59 | $265.03 |
| IQV | 2 | $255.46 | $275.04 | $550.08 | $39.17 | $247.54 |
| MPC | 3 | $399.06 | $390.77 | $1,172.31 | $-24.86 | $358.97 |
| NTAP | 5 | $206.27 | $197.24 | $986.20 | $-45.15 | $179.40 |
| PSX | 5 | $215.50 | $255.89 | $1,279.45 | $201.97 | $246.58 |
| RVTY | 9 | $122.75 | $150.71 | $1,356.39 | $251.67 | $135.64 |
| SPY | 5 | $743.10 | $767.29 | $3,836.45 | $120.95 | — |
| TECH | 12 | $72.32 | $72.56 | $870.72 | $2.88 | $65.30 |
| TGT | 7 | $162.82 | $156.28 | $1,093.96 | $-45.75 | $147.91 |
| VLO | 3 | $392.61 | $383.02 | $1,149.06 | $-28.76 | $352.71 |
| ZBRA | 3 | $345.13 | $365.37 | $1,096.11 | $60.73 | $333.97 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-09-24T17:55` entry buy **VLO** — momentum entry: rank 2, mom 0.681, vol 32%
- `2026-09-24T17:55` entry buy **MPC** — momentum entry: rank 1, mom 0.714, vol 30%
- `2026-09-23T21:42` system — eod_complete
- `2026-09-23T17:56` no_trade skip_entry **SOLV** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **EXPD** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **ADP** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **WAT** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **FFIV** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **TMO** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **VLO** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` no_trade skip_entry **MPC** — insufficient investable cash (size $37, need >= $500)
- `2026-09-23T17:56` exit sell **GEN** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-23T17:56` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-09-23T17:56` exit sell **VLO** — trailing stop 10%
- `2026-09-23T17:56` exit sell **MPC** — trailing stop 10%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
