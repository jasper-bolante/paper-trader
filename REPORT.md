# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-18 17:56 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,870.72** |
| Total return since inception | -0.65% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,798.01 (3.99%) |
| Positions value | $17,838.77 |
| Settled cash | $2,029.92 |
| Unsettled cash (T+1) | $9.95 |
| Tax reserve | $7.92 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.87% | 3.81% |
| Annualized volatility | 12.53% | 13.38% |
| Sharpe (rf 4%) | -0.89 | 2.28 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 29 | 29 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $25.89 | $724.92 | $-38.69 | $25.00 |
| BBY | 14 | $88.05 | $87.86 | $1,230.04 | $-2.71 | $79.24 |
| CNC | 8 | $75.27 | $65.35 | $522.80 | $-79.33 | $58.73 |
| CRL | 2 | $285.12 | $282.10 | $564.20 | $-6.04 | $258.00 |
| CSX | 17 | $50.29 | $50.34 | $855.87 | $0.91 | $46.01 |
| FTNT | 7 | $149.43 | $157.68 | $1,103.76 | $57.72 | $151.44 |
| HUM | 2 | $398.00 | $383.16 | $766.32 | $-29.67 | $350.32 |
| MPC | 3 | $306.56 | $364.94 | $1,094.82 | $175.14 | $322.39 |
| NTAP | 5 | $161.48 | $205.53 | $1,027.65 | $220.27 | $186.39 |
| NUE | 2 | $269.82 | $264.00 | $528.00 | $-11.64 | $245.50 |
| PANW | 2 | $388.28 | $374.30 | $748.60 | $-27.96 | $349.27 |
| PSX | 5 | $215.50 | $241.78 | $1,208.88 | $131.39 | $216.44 |
| SPY | 5 | $743.10 | $767.95 | $3,839.75 | $124.25 | — |
| STT | 8 | $185.86 | $192.26 | $1,538.08 | $51.21 | $173.64 |
| VLO | 3 | $304.72 | $348.98 | $1,046.94 | $132.78 | $312.28 |
| WST | 3 | $336.32 | $346.05 | $1,038.15 | $29.19 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $52.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-18T17:56` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T17:56` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T16:59` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T16:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T15:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T15:58` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T15:03` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T15:03` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T14:08` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T14:08` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T14:07` system **PSX** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-17T20:56` system — eod_complete
- `2026-08-17T20:56` system — corporate_actions_synced
- `2026-08-17T19:53` no_trade — no signals crossed action thresholds this hour
- `2026-08-17T19:53` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
