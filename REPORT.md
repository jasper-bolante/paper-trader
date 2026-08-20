# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-20 19:11 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,573.30** |
| Total return since inception | -2.13% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,700.58 (3.50%) |
| Positions value | $15,940.08 |
| Settled cash | $1,356.79 |
| Unsettled cash (T+1) | $2,284.80 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.50% | 3.32% |
| Annualized volatility | 12.28% | 13.14% |
| Sharpe (rf 4%) | -1.30 | 1.85 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 31 | 31 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.36 | $738.22 | $-25.39 | $25.00 |
| BBY | 14 | $88.05 | $85.39 | $1,195.46 | $-37.29 | $80.33 |
| CRL | 2 | $285.12 | $295.71 | $591.42 | $21.18 | $260.98 |
| CSX | 17 | $50.29 | $51.05 | $867.85 | $12.90 | $46.01 |
| EXPE | 2 | $331.47 | $325.12 | $650.24 | $-12.70 | $298.17 |
| IQV | 2 | $255.46 | $258.85 | $517.70 | $6.79 | $229.79 |
| MPC | 3 | $306.56 | $357.05 | $1,071.15 | $151.47 | $330.10 |
| NTAP | 5 | $161.48 | $193.90 | $969.50 | $162.12 | $186.39 |
| PSX | 5 | $215.50 | $240.31 | $1,201.55 | $124.07 | $219.13 |
| SPY | 5 | $743.10 | $763.45 | $3,817.25 | $101.75 | — |
| STT | 8 | $185.86 | $184.52 | $1,476.16 | $-10.71 | $173.64 |
| VEEV | 3 | $250.82 | $250.56 | $751.68 | $-0.79 | $225.62 |
| VLO | 3 | $304.72 | $341.26 | $1,023.78 | $109.62 | $315.01 |
| WST | 3 | $336.32 | $356.04 | $1,068.12 | $59.16 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,136.32 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-20T19:11` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` exit sell **PANW** — trailing stop 10%
- `2026-08-20T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:58` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:02` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T16:01` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T16:01` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T15:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T15:07` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T14:10` entry buy **IQV** — momentum entry: rank 10, mom 0.353, vol 50%
- `2026-08-20T14:10` entry buy **VEEV** — momentum entry: rank 7, mom 0.403, vol 41%
- `2026-08-20T14:10` exit sell **CNC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-20T14:09` exit sell **FTNT** — trailing stop 10%
- `2026-08-19T20:56` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
