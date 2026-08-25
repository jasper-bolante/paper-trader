# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-25 16:09 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,612.49** |
| Total return since inception | -1.94% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,553.09 (2.77%) |
| Positions value | $17,097.01 |
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
| BAX | 28 | $27.27 | $26.27 | $735.42 | $-28.19 | $25.00 |
| BBY | 14 | $88.05 | $85.46 | $1,196.44 | $-36.31 | $80.33 |
| CRL | 2 | $285.12 | $298.65 | $597.31 | $27.07 | $268.70 |
| CSX | 17 | $50.29 | $51.58 | $876.86 | $21.91 | $46.44 |
| EXPE | 2 | $331.47 | $335.09 | $670.18 | $7.24 | $305.24 |
| FDS | 2 | $299.76 | $301.00 | $602.00 | $2.47 | $274.51 |
| IQV | 2 | $255.46 | $258.99 | $517.98 | $7.07 | $234.27 |
| MPC | 3 | $306.56 | $360.23 | $1,080.69 | $161.01 | $330.10 |
| NTAP | 4 | $187.95 | $187.37 | $749.48 | $-2.31 | $169.07 |
| PANW | 2 | $388.17 | $345.23 | $690.46 | $-85.88 | $322.11 |
| PSX | 5 | $215.50 | $240.10 | $1,200.50 | $123.02 | $219.13 |
| SPY | 5 | $743.10 | $765.37 | $3,826.85 | $111.35 | — |
| STT | 8 | $185.86 | $192.26 | $1,538.08 | $51.21 | $173.64 |
| VEEV | 3 | $250.82 | $244.24 | $732.72 | $-19.75 | $225.63 |
| VLO | 3 | $304.72 | $343.76 | $1,031.30 | $117.14 | $315.01 |
| WST | 3 | $336.32 | $350.25 | $1,050.75 | $41.79 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-24T18:00` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T18:00` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-24T17:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T17:07` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
