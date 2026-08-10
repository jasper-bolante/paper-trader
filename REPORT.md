# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-10 18:25 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,681.06** |
| Total return since inception | -1.59% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,809.04 (4.05%) |
| Positions value | $18,640.95 |
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
| BAX | 28 | $27.27 | $27.82 | $778.96 | $15.35 | $24.79 |
| BBY | 14 | $88.05 | $82.61 | $1,156.54 | $-76.21 | $79.24 |
| CSCO | 8 | $131.57 | $124.25 | $994.04 | $-58.55 | $109.28 |
| CSX | 17 | $50.29 | $50.20 | $853.32 | $-1.63 | $46.01 |
| DDOG | 3 | $268.94 | $256.06 | $768.18 | $-38.64 | $211.93 |
| DOC | 40 | $21.90 | $21.00 | $839.80 | $-36.27 | $18.97 |
| FTNT | 7 | $149.43 | $164.66 | $1,152.65 | $106.62 | $151.44 |
| HPQ | 31 | $28.20 | $30.25 | $937.60 | $63.36 | $27.04 |
| HUM | 2 | $398.00 | $387.60 | $775.20 | $-20.79 | $348.07 |
| MPC | 3 | $306.56 | $316.60 | $949.80 | $30.12 | $287.83 |
| NTAP | 5 | $161.48 | $200.83 | $1,004.15 | $196.77 | $172.38 |
| PSX | 5 | $215.50 | $214.15 | $1,070.73 | $-6.75 | $191.32 |
| SPY | 5 | $743.10 | $772.60 | $3,863.00 | $147.50 | — |
| STT | 8 | $185.86 | $185.57 | $1,484.56 | $-2.31 | $168.31 |
| VLO | 3 | $304.72 | $314.71 | $944.13 | $29.97 | $283.28 |
| WST | 3 | $336.32 | $356.10 | $1,068.30 | $59.34 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-765.33 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-08-07T17:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T17:26` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
