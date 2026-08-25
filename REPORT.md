# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-25 17:59 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,591.28** |
| Total return since inception | -2.04% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,553.09 (2.77%) |
| Positions value | $17,075.81 |
| Settled cash | $2,510.89 |
| Unsettled cash (T+1) | $12.95 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.58% | 2.58% |
| Annualized volatility | 12.09% | 12.84% |
| Sharpe (rf 4%) | -1.28 | 1.27 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 34 | 34 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.39 | $738.92 | $-24.69 | $25.00 |
| BBY | 14 | $88.05 | $85.77 | $1,200.78 | $-31.97 | $80.33 |
| CRL | 2 | $285.12 | $297.94 | $595.88 | $25.64 | $268.70 |
| CSX | 17 | $50.29 | $51.31 | $872.27 | $17.32 | $46.44 |
| EXPE | 2 | $331.47 | $335.73 | $671.46 | $8.52 | $305.24 |
| FDS | 2 | $299.76 | $301.06 | $602.13 | $2.60 | $274.51 |
| IQV | 2 | $255.46 | $258.89 | $517.78 | $6.87 | $234.27 |
| MPC | 3 | $306.56 | $359.16 | $1,077.48 | $157.80 | $330.10 |
| NTAP | 4 | $187.95 | $186.90 | $747.60 | $-4.19 | $169.07 |
| PANW | 2 | $388.17 | $338.35 | $676.70 | $-99.64 | $322.11 |
| PSX | 5 | $215.50 | $239.95 | $1,199.75 | $122.27 | $219.13 |
| SPY | 5 | $743.10 | $765.09 | $3,825.45 | $109.95 | — |
| STT | 8 | $185.86 | $191.75 | $1,534.04 | $47.17 | $173.64 |
| VEEV | 3 | $250.82 | $243.17 | $729.51 | $-22.96 | $225.63 |
| VLO | 3 | $304.72 | $343.76 | $1,031.30 | $117.14 | $315.01 |
| WST | 3 | $336.32 | $351.59 | $1,054.77 | $45.81 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-25T17:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T17:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T17:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T17:07` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T16:09` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T16:09` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T15:23` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T15:23` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T14:22` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T14:22` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-24T21:00` system — eod_complete
- `2026-08-24T19:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T19:56` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-24T19:10` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T19:10` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
