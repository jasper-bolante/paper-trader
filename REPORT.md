# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-16 16:50 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,891.52** |
| Total return since inception | -0.54% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,314.09 (1.57%) |
| Positions value | $17,479.72 |
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
| BEN | 42 | $33.14 | $33.49 | $1,406.58 | $14.62 | $30.26 |
| CNC | 13 | $66.94 | $65.56 | $852.22 | $-18.02 | $61.84 |
| DDOG | 3 | $260.67 | $261.00 | $783.00 | $1.00 | $234.48 |
| DVA | 6 | $227.39 | $236.29 | $1,417.74 | $53.38 | $211.95 |
| FFIV | 3 | $430.59 | $402.00 | $1,206.01 | $-85.76 | $388.22 |
| FTNT | 5 | $155.14 | $159.38 | $796.90 | $21.22 | $150.16 |
| HUM | 2 | $401.64 | $392.81 | $785.62 | $-17.66 | $366.83 |
| IBKR | 10 | $95.61 | $92.64 | $926.35 | $-29.71 | $87.64 |
| MPC | 3 | $306.56 | $305.21 | $915.63 | $-4.05 | $275.76 |
| NTAP | 5 | $161.48 | $158.18 | $790.88 | $-16.50 | $145.92 |
| SPY | 5 | $743.10 | $752.25 | $3,761.28 | $45.78 | — |
| STT | 8 | $185.86 | $183.81 | $1,470.52 | $-16.35 | $168.04 |
| UNH | 3 | $425.21 | $432.56 | $1,297.68 | $22.06 | $382.79 |
| URI | 1 | $1,090.35 | $1,069.32 | $1,069.32 | $-21.03 | $980.79 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-89.61 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-15T15:09` entry buy **STT** — momentum entry: rank 11, mom 0.388, vol 25%
- `2026-07-15T15:09` entry buy **NTAP** — momentum entry: rank 5, mom 0.600, vol 44%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
