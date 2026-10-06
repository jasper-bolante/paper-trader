# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-10-06 01:43 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,226.08** |
| Total return since inception | 1.13% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,851.57 (4.26%) |
| Positions value | $18,881.51 |
| Settled cash | $1,341.92 |
| Unsettled cash (T+1) | $17.12 |
| Tax reserve | $14.47 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 1.06% | 4.07% |
| Annualized volatility | 11.21% | 11.30% |
| Sharpe (rf 4%) | 0.08 | 1.14 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 63 | 63 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| ANET | 4 | $191.78 | $206.97 | $827.86 | $60.74 | $186.60 |
| APA | 19 | $44.15 | $43.86 | $833.34 | $-5.55 | $39.73 |
| BBY | 8 | $101.21 | $87.39 | $699.08 | $-110.60 | $85.36 |
| CRL | 3 | $296.67 | $310.95 | $932.87 | $42.85 | $279.86 |
| FFIV | 2 | $448.44 | $458.21 | $916.42 | $19.53 | $412.39 |
| IQV | 2 | $255.46 | $266.04 | $532.08 | $21.17 | $247.54 |
| MPC | 3 | $399.06 | $433.52 | $1,300.57 | $103.40 | $390.17 |
| NTAP | 5 | $206.27 | $223.91 | $1,119.55 | $88.20 | $203.86 |
| PSX | 5 | $215.50 | $269.70 | $1,348.50 | $271.02 | $246.58 |
| RVTY | 9 | $122.75 | $157.41 | $1,416.69 | $311.97 | $141.67 |
| SPY | 5 | $743.10 | $774.74 | $3,873.70 | $158.20 | — |
| TECH | 12 | $72.32 | $72.60 | $871.20 | $3.36 | $65.36 |
| TGT | 7 | $162.82 | $153.00 | $1,071.00 | $-68.71 | $147.91 |
| VLO | 3 | $392.61 | $419.38 | $1,258.15 | $80.34 | $377.45 |
| WST | 2 | $370.69 | $376.77 | $753.54 | $12.16 | $339.09 |
| ZBRA | 3 | $345.13 | $375.65 | $1,126.95 | $91.57 | $338.33 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-935.56 | $0.00 | $1,142.35 |

Dividends received: $96.45. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-10-02T23:11` system — eod_complete
- `2026-10-02T18:39` no_trade — no signals crossed action thresholds this hour
- `2026-10-02T18:39` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-10-01T23:22` system — eod_complete
- `2026-10-01T18:59` no_trade — no signals crossed action thresholds this hour
- `2026-10-01T18:59` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-09-30T22:32` system — eod_complete
- `2026-09-30T18:31` no_trade — no signals crossed action thresholds this hour
- `2026-09-30T18:31` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-09-29T23:08` system — eod_complete
- `2026-09-29T23:08` system — corporate_actions_synced
- `2026-09-29T18:49` no_trade — no signals crossed action thresholds this hour
- `2026-09-29T18:49` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-09-28T20:12` system — eod_complete
- `2026-09-25T21:46` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
