# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-25 17:07 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,619.88** |
| Total return since inception | -1.90% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,553.09 (2.77%) |
| Positions value | $17,104.41 |
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
| BAX | 28 | $27.27 | $26.29 | $736.12 | $-27.49 | $25.00 |
| BBY | 14 | $88.05 | $85.86 | $1,202.11 | $-30.64 | $80.33 |
| CRL | 2 | $285.12 | $298.14 | $596.28 | $26.04 | $268.70 |
| CSX | 17 | $50.29 | $51.38 | $873.46 | $18.51 | $46.44 |
| EXPE | 2 | $331.47 | $335.88 | $671.75 | $8.81 | $305.24 |
| FDS | 2 | $299.76 | $300.67 | $601.33 | $1.80 | $274.51 |
| IQV | 2 | $255.46 | $258.96 | $517.92 | $7.01 | $234.27 |
| MPC | 3 | $306.56 | $360.43 | $1,081.29 | $161.61 | $330.10 |
| NTAP | 4 | $187.95 | $186.67 | $746.68 | $-5.11 | $169.07 |
| PANW | 2 | $388.17 | $343.74 | $687.48 | $-88.86 | $322.11 |
| PSX | 5 | $215.50 | $240.77 | $1,203.85 | $126.37 | $219.13 |
| SPY | 5 | $743.10 | $765.30 | $3,826.52 | $111.02 | — |
| STT | 8 | $185.86 | $192.04 | $1,536.36 | $49.49 | $173.64 |
| VEEV | 3 | $250.82 | $244.42 | $733.26 | $-19.21 | $225.63 |
| VLO | 3 | $304.72 | $346.06 | $1,038.16 | $124.00 | $315.01 |
| WST | 3 | $336.32 | $350.61 | $1,051.83 | $42.87 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-933.79 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-24T18:00` no_trade — no signals crossed action thresholds this hour
- `2026-08-24T18:00` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
