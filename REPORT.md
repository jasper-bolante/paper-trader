# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-16 20:29 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,839.23** |
| Total return since inception | -0.80% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,209.12 (1.05%) |
| Positions value | $17,427.42 |
| Settled cash | $1,527.74 |
| Unsettled cash (T+1) | $889.73 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -0.87% | 0.87% |
| Annualized volatility | 8.74% | 10.38% |
| Sharpe (rf 4%) | -4.62 | 3.16 |
| Max drawdown | 1.50% | 0.77% |
| EOD observations | 7 | 7 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BEN | 42 | $33.14 | $33.33 | $1,399.86 | $7.90 | $30.26 |
| CNC | 13 | $66.94 | $63.91 | $830.76 | $-39.48 | $61.84 |
| DDOG | 3 | $260.67 | $262.29 | $786.87 | $4.87 | $236.06 |
| DVA | 6 | $227.39 | $233.82 | $1,402.92 | $38.56 | $211.95 |
| FFIV | 3 | $430.59 | $403.57 | $1,210.71 | $-81.06 | $388.22 |
| FTNT | 5 | $155.14 | $160.81 | $804.03 | $28.35 | $150.16 |
| HUM | 2 | $401.64 | $386.20 | $772.40 | $-30.88 | $366.83 |
| IBKR | 10 | $95.61 | $92.20 | $922.00 | $-34.06 | $87.64 |
| MPC | 3 | $306.56 | $306.09 | $918.27 | $-1.41 | $275.76 |
| NTAP | 5 | $161.48 | $159.65 | $798.23 | $-9.15 | $145.92 |
| SPY | 5 | $743.10 | $750.87 | $3,754.35 | $38.85 | — |
| STT | 8 | $185.86 | $185.62 | $1,484.96 | $-1.91 | $168.04 |
| UNH | 3 | $425.21 | $423.28 | $1,269.84 | $-5.78 | $382.79 |
| URI | 1 | $1,090.35 | $1,072.23 | $1,072.23 | $-18.12 | $980.79 |

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
