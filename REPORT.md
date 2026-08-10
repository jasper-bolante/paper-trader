# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-10 20:17 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,656.67** |
| Total return since inception | -1.72% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,799.89 (4.00%) |
| Positions value | $18,616.56 |
| Settled cash | $1,043.31 |
| Unsettled cash (T+1) | $3.60 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.78% | 3.82% |
| Annualized volatility | 13.07% | 14.44% |
| Sharpe (rf 4%) | -1.75 | 2.64 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 24 | 24 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.78 | $777.84 | $14.23 | $25.00 |
| BBY | 14 | $88.05 | $82.42 | $1,153.88 | $-78.87 | $79.24 |
| CSCO | 8 | $131.57 | $122.61 | $980.84 | $-71.75 | $110.34 |
| CSX | 17 | $50.29 | $50.15 | $852.55 | $-2.40 | $46.01 |
| DDOG | 3 | $268.94 | $260.74 | $782.22 | $-24.60 | $234.67 |
| DOC | 40 | $21.90 | $20.91 | $836.40 | $-39.67 | $18.97 |
| FTNT | 7 | $149.43 | $164.16 | $1,149.15 | $103.12 | $151.44 |
| HPQ | 31 | $28.20 | $29.81 | $924.11 | $49.87 | $27.04 |
| HUM | 2 | $398.00 | $385.34 | $770.68 | $-25.31 | $348.07 |
| MPC | 3 | $306.56 | $320.27 | $960.81 | $41.13 | $288.24 |
| NTAP | 5 | $161.48 | $198.72 | $993.60 | $186.22 | $178.85 |
| PSX | 5 | $215.50 | $215.35 | $1,076.75 | $-0.73 | $193.81 |
| SPY | 5 | $743.10 | $772.82 | $3,864.10 | $148.60 | — |
| STT | 8 | $185.86 | $186.54 | $1,492.32 | $5.45 | $168.31 |
| VLO | 3 | $304.72 | $314.97 | $944.91 | $30.75 | $283.47 |
| WST | 3 | $336.32 | $352.13 | $1,056.39 | $47.43 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-765.33 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-10T19:33` no_trade — no signals crossed action thresholds this hour
- `2026-08-10T19:33` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-10T18:25` no_trade — no signals crossed action thresholds this hour
- `2026-08-10T18:25` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-10T17:28` no_trade — no signals crossed action thresholds this hour
- `2026-08-10T17:28` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-10T16:25` no_trade — no signals crossed action thresholds this hour
- `2026-08-10T16:25` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-10T14:38` entry buy **DOC** — momentum entry: rank 11, mom 0.312, vol 21%
- `2026-08-10T14:38` entry buy **HUM** — momentum entry: rank 3, mom 0.695, vol 39%
- `2026-08-07T20:10` system — eod_complete
- `2026-08-07T19:33` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T19:33` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T18:25` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T18:25` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
