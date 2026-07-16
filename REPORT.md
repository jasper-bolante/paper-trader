# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-16 18:43 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,869.37** |
| Total return since inception | -0.65% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,314.09 (1.57%) |
| Positions value | $17,457.56 |
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
| BEN | 42 | $33.14 | $33.30 | $1,398.60 | $6.64 | $30.26 |
| CNC | 13 | $66.94 | $65.23 | $847.99 | $-22.25 | $61.84 |
| DDOG | 3 | $260.67 | $262.61 | $787.83 | $5.83 | $234.48 |
| DVA | 6 | $227.39 | $235.41 | $1,412.43 | $48.07 | $211.95 |
| FFIV | 3 | $430.59 | $402.47 | $1,207.41 | $-84.36 | $388.22 |
| FTNT | 5 | $155.14 | $161.62 | $808.10 | $32.42 | $150.16 |
| HUM | 2 | $401.64 | $395.94 | $791.88 | $-11.40 | $366.83 |
| IBKR | 10 | $95.61 | $91.71 | $917.10 | $-38.96 | $87.64 |
| MPC | 3 | $306.56 | $308.15 | $924.45 | $4.77 | $275.76 |
| NTAP | 5 | $161.48 | $159.14 | $795.70 | $-11.68 | $145.92 |
| SPY | 5 | $743.10 | $750.55 | $3,752.75 | $37.25 | — |
| STT | 8 | $185.86 | $183.19 | $1,465.48 | $-21.39 | $168.04 |
| UNH | 3 | $425.21 | $427.46 | $1,282.39 | $6.78 | $382.79 |
| URI | 1 | $1,090.35 | $1,065.45 | $1,065.45 | $-24.90 | $980.79 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-89.61 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-16T18:43` no_trade — no signals crossed action thresholds this hour
- `2026-07-16T18:43` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-07-16T16:50` no_trade — no signals crossed action thresholds this hour
- `2026-07-16T16:50` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
