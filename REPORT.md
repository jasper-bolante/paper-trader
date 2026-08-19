# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-19 15:03 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,854.86** |
| Total return since inception | -0.73% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,652.67 (3.26%) |
| Positions value | $17,717.71 |
| Settled cash | $1,366.98 |
| Unsettled cash (T+1) | $778.54 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.75% | 3.08% |
| Annualized volatility | 12.31% | 13.37% |
| Sharpe (rf 4%) | -0.80 | 1.74 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 30 | 30 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.55 | $743.40 | $-20.21 | $25.00 |
| BBY | 14 | $88.05 | $89.75 | $1,256.43 | $23.68 | $79.24 |
| CNC | 8 | $75.27 | $64.67 | $517.36 | $-84.77 | $58.73 |
| CRL | 2 | $285.12 | $290.37 | $580.73 | $10.49 | $258.00 |
| CSX | 17 | $50.29 | $51.16 | $869.72 | $14.77 | $46.01 |
| EXPE | 2 | $331.47 | $331.64 | $663.28 | $0.34 | $298.17 |
| FTNT | 7 | $149.43 | $153.23 | $1,072.61 | $26.57 | $151.44 |
| MPC | 3 | $306.56 | $363.33 | $1,089.99 | $170.31 | $330.10 |
| NTAP | 5 | $161.48 | $198.43 | $992.15 | $184.77 | $186.39 |
| NUE | 2 | $269.82 | $263.08 | $526.17 | $-13.47 | $245.50 |
| PANW | 2 | $388.28 | $356.11 | $712.22 | $-64.34 | $349.27 |
| PSX | 5 | $215.50 | $243.14 | $1,215.70 | $138.22 | $219.13 |
| SPY | 5 | $743.10 | $772.06 | $3,860.30 | $144.80 | — |
| STT | 8 | $185.86 | $188.87 | $1,510.96 | $24.09 | $173.64 |
| VLO | 3 | $304.72 | $348.24 | $1,044.70 | $130.54 | $315.01 |
| WST | 3 | $336.32 | $354.00 | $1,061.99 | $53.03 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-931.39 | $0.00 | $458.50 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-19T15:03` no_trade — no signals crossed action thresholds this hour
- `2026-08-19T15:03` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-19T14:08` entry buy **EXPE** — momentum entry: rank 9, mom 0.404, vol 42%
- `2026-08-19T14:08` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-19T14:08` system **MPC** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-18T20:52` system — eod_complete
- `2026-08-18T19:50` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T19:50` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T19:08` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T19:08` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T17:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T17:56` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T16:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T16:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T15:58` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
