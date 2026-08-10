# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-10 17:28 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,674.78** |
| Total return since inception | -1.63% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,809.04 (4.05%) |
| Positions value | $18,634.67 |
| Settled cash | $1,043.31 |
| Unsettled cash (T+1) | $3.60 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -3.50% | 3.86% |
| Annualized volatility | 11.65% | 14.76% |
| Sharpe (rf 4%) | -3.79 | 2.74 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 23 | 23 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.72 | $776.16 | $12.55 | $24.79 |
| BBY | 14 | $88.05 | $82.23 | $1,151.29 | $-81.46 | $79.24 |
| CSCO | 8 | $131.57 | $124.17 | $993.32 | $-59.27 | $109.28 |
| CSX | 17 | $50.29 | $50.22 | $853.66 | $-1.29 | $46.01 |
| DDOG | 3 | $268.94 | $256.86 | $770.58 | $-36.24 | $211.93 |
| DOC | 40 | $21.90 | $21.00 | $840.20 | $-35.87 | $18.97 |
| FTNT | 7 | $149.43 | $165.25 | $1,156.78 | $110.74 | $151.44 |
| HPQ | 31 | $28.20 | $30.25 | $937.90 | $63.66 | $27.04 |
| HUM | 2 | $398.00 | $387.11 | $774.22 | $-21.77 | $348.07 |
| MPC | 3 | $306.56 | $315.48 | $946.44 | $26.76 | $287.83 |
| NTAP | 5 | $161.48 | $200.80 | $1,004.00 | $196.62 | $172.38 |
| PSX | 5 | $215.50 | $213.52 | $1,067.60 | $-9.88 | $191.32 |
| SPY | 5 | $743.10 | $773.01 | $3,865.05 | $149.55 | — |
| STT | 8 | $185.86 | $185.53 | $1,484.20 | $-2.67 | $168.31 |
| VLO | 3 | $304.72 | $313.83 | $941.49 | $27.33 | $283.28 |
| WST | 3 | $336.32 | $357.26 | $1,071.78 | $62.82 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-765.33 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-07T17:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T17:26` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T16:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T16:26` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
