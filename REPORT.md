# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-16 15:18 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,996.60** |
| Total return since inception | -0.02% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,314.09 (1.57%) |
| Positions value | $17,584.79 |
| Settled cash | $1,527.74 |
| Unsettled cash (T+1) | $889.73 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.24% | 1.39% |
| Annualized volatility | 5.09% | 10.07% |
| Sharpe (rf 4%) | 1.57 | 6.57 |
| Max drawdown | 0.40% | 0.77% |
| EOD observations | 6 | 6 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BEN | 42 | $33.14 | $33.61 | $1,411.62 | $19.66 | $30.26 |
| CNC | 13 | $66.94 | $65.90 | $856.70 | $-13.54 | $61.84 |
| DDOG | 3 | $260.67 | $260.53 | $781.59 | $-0.41 | $234.48 |
| DVA | 6 | $227.39 | $235.56 | $1,413.33 | $48.97 | $211.95 |
| FFIV | 3 | $430.59 | $403.18 | $1,209.54 | $-82.23 | $388.22 |
| FTNT | 5 | $155.14 | $162.35 | $811.75 | $36.07 | $150.16 |
| HUM | 2 | $401.64 | $401.95 | $803.90 | $0.62 | $366.83 |
| IBKR | 10 | $95.61 | $93.54 | $935.40 | $-20.66 | $87.64 |
| MPC | 3 | $306.56 | $306.40 | $919.20 | $-0.48 | $275.76 |
| NTAP | 5 | $161.48 | $158.40 | $792.00 | $-15.38 | $145.92 |
| SPY | 5 | $743.10 | $753.33 | $3,766.65 | $51.15 | — |
| STT | 8 | $185.86 | $186.88 | $1,495.04 | $8.17 | $168.04 |
| UNH | 3 | $425.21 | $438.02 | $1,314.07 | $38.45 | $382.79 |
| URI | 1 | $1,090.35 | $1,074.00 | $1,074.00 | $-16.35 | $980.79 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-89.61 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-16T15:18` entry buy **MPC** — momentum entry: rank 9, mom 0.374, vol 34%
- `2026-07-16T15:18` entry buy **DDOG** — momentum entry: rank 1, mom 1.097, vol 48%
- `2026-07-16T15:18` exit sell **CSCO** — trailing stop 10%
- `2026-07-15T20:36` system — eod_complete
- `2026-07-15T20:36` system **NTAP** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-15T20:36` system **STT** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-15T20:36` system — corporate_actions_synced
- `2026-07-15T18:40` no_trade — no signals crossed action thresholds this hour
- `2026-07-15T18:40` no_trade skip_entry — no entry slots (positions 12/15, new today 2/2)
- `2026-07-15T16:52` no_trade — no signals crossed action thresholds this hour
- `2026-07-15T16:52` no_trade skip_entry — no entry slots (positions 12/15, new today 2/2)
- `2026-07-15T15:09` entry buy **STT** — momentum entry: rank 11, mom 0.388, vol 25%
- `2026-07-15T15:09` entry buy **NTAP** — momentum entry: rank 5, mom 0.600, vol 44%
- `2026-07-14T20:40` system — eod_complete
- `2026-07-14T18:42` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
