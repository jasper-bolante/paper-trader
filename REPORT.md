# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-18 19:50 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,884.71** |
| Total return since inception | -0.58% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,798.01 (3.99%) |
| Positions value | $17,852.76 |
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
| BAX | 28 | $27.27 | $26.02 | $728.42 | $-35.19 | $25.00 |
| BBY | 14 | $88.05 | $87.31 | $1,222.41 | $-10.34 | $79.24 |
| CNC | 8 | $75.27 | $65.33 | $522.64 | $-79.49 | $58.73 |
| CRL | 2 | $285.12 | $280.81 | $561.63 | $-8.61 | $258.00 |
| CSX | 17 | $50.29 | $50.30 | $855.10 | $0.15 | $46.01 |
| FTNT | 7 | $149.43 | $158.37 | $1,108.59 | $62.55 | $151.44 |
| HUM | 2 | $398.00 | $384.17 | $768.34 | $-27.65 | $350.32 |
| MPC | 3 | $306.56 | $366.62 | $1,099.86 | $180.18 | $322.39 |
| NTAP | 5 | $161.48 | $206.24 | $1,031.18 | $223.80 | $186.39 |
| NUE | 2 | $269.82 | $264.86 | $529.72 | $-9.92 | $245.50 |
| PANW | 2 | $388.28 | $373.67 | $747.33 | $-29.23 | $349.27 |
| PSX | 5 | $215.50 | $242.69 | $1,213.45 | $135.97 | $216.44 |
| SPY | 5 | $743.10 | $767.73 | $3,838.62 | $123.12 | — |
| STT | 8 | $185.86 | $192.06 | $1,536.48 | $49.61 | $173.64 |
| VLO | 3 | $304.72 | $350.29 | $1,050.87 | $136.71 | $312.28 |
| WST | 3 | $336.32 | $346.04 | $1,038.12 | $29.16 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-900.98 | $0.00 | $458.50 |

Dividends received: $52.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-18T19:50` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T19:50` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-18T19:08` no_trade — no signals crossed action thresholds this hour
- `2026-08-18T19:08` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
