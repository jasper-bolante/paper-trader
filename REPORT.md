# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-26 18:18 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,696.44** |
| Total return since inception | -1.52% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,612.30 (3.06%) |
| Positions value | $16,930.00 |
| Settled cash | $1,716.01 |
| Unsettled cash (T+1) | $1,058.80 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.26% | 2.88% |
| Annualized volatility | 12.03% | 12.65% |
| Sharpe (rf 4%) | -1.68 | 1.41 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 35 | 35 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.68 | $747.18 | $-16.43 | $25.00 |
| BBY | 14 | $88.05 | $87.59 | $1,226.26 | $-6.49 | $80.33 |
| CRL | 2 | $285.12 | $296.97 | $593.94 | $23.70 | $268.70 |
| CSX | 17 | $50.29 | $51.98 | $883.58 | $28.62 | $46.44 |
| EXPE | 2 | $331.47 | $337.50 | $675.00 | $12.06 | $305.24 |
| FDS | 2 | $299.76 | $295.27 | $590.54 | $-8.99 | $274.51 |
| HUM | 2 | $406.24 | $389.96 | $779.93 | $-32.54 | $357.63 |
| IQV | 2 | $255.46 | $261.60 | $523.20 | $12.29 | $234.27 |
| MPC | 3 | $306.56 | $361.86 | $1,085.58 | $165.90 | $330.10 |
| NTAP | 4 | $187.95 | $193.30 | $773.20 | $21.41 | $169.07 |
| PANW | 2 | $388.17 | $339.87 | $679.74 | $-96.60 | $322.11 |
| PSX | 5 | $215.50 | $242.29 | $1,211.45 | $133.97 | $219.13 |
| SPY | 5 | $743.10 | $765.62 | $3,828.12 | $112.62 | — |
| STT | 8 | $185.86 | $193.62 | $1,548.96 | $62.09 | $173.74 |
| VEEV | 3 | $250.82 | $247.00 | $741.00 | $-11.47 | $225.63 |
| VLO | 3 | $304.72 | $347.44 | $1,042.32 | $128.16 | $315.01 |

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
