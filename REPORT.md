# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-26 21:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,677.62** |
| Total return since inception | -1.61% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,627.64 (3.14%) |
| Positions value | $16,911.17 |
| Settled cash | $1,716.01 |
| Unsettled cash (T+1) | $1,058.80 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.68% | 2.96% |
| Annualized volatility | 11.98% | 12.47% |
| Sharpe (rf 4%) | -1.29 | 1.42 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 36 | 36 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.49 | $741.72 | $-21.89 | $25.00 |
| BBY | 14 | $88.05 | $87.45 | $1,224.30 | $-8.45 | $80.33 |
| CRL | 2 | $285.12 | $295.21 | $590.42 | $20.18 | $268.70 |
| CSX | 17 | $50.29 | $51.76 | $879.92 | $24.97 | $46.58 |
| EXPE | 2 | $331.47 | $333.31 | $666.61 | $3.67 | $305.24 |
| FDS | 2 | $299.76 | $295.41 | $590.82 | $-8.71 | $274.51 |
| HUM | 2 | $406.24 | $391.01 | $782.03 | $-30.44 | $357.63 |
| IQV | 2 | $255.46 | $261.58 | $523.16 | $12.25 | $235.42 |
| MPC | 3 | $306.56 | $362.26 | $1,086.80 | $167.12 | $330.10 |
| NTAP | 4 | $187.95 | $193.91 | $775.64 | $23.85 | $174.52 |
| PANW | 2 | $388.17 | $339.40 | $678.80 | $-97.54 | $322.11 |
| PSX | 5 | $215.50 | $242.29 | $1,211.45 | $133.97 | $219.13 |
| SPY | 5 | $743.10 | $766.42 | $3,832.10 | $116.60 | — |
| STT | 8 | $185.86 | $193.54 | $1,548.32 | $61.45 | $174.19 |
| VEEV | 3 | $250.82 | $245.10 | $735.30 | $-17.17 | $225.63 |
| VLO | 3 | $304.72 | $347.93 | $1,043.79 | $129.63 | $315.01 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-879.32 | $0.00 | $554.53 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-26T18:18` no_trade — no signals crossed action thresholds this hour
- `2026-08-26T18:18` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-26T16:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-26T16:02` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-26T14:20` entry buy **HUM** — momentum entry: rank 4, mom 0.657, vol 38%
- `2026-08-26T14:20` exit sell **WST** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-25T20:57` system — eod_complete
- `2026-08-25T19:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T19:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T19:09` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T19:09` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T17:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T17:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T17:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T17:07` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
