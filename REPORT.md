# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-15 20:36 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,060.81** |
| Total return since inception | 0.30% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,314.09 (1.57%) |
| Positions value | $16,819.81 |
| Settled cash | $3,229.42 |
| Unsettled cash (T+1) | $17.25 |
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
| BEN | 42 | $33.14 | $33.62 | $1,412.04 | $20.08 | $30.26 |
| CNC | 13 | $66.94 | $66.59 | $865.74 | $-4.50 | $61.84 |
| CSCO | 8 | $120.26 | $111.76 | $894.08 | $-68.01 | $109.12 |
| DVA | 6 | $227.39 | $231.82 | $1,390.92 | $26.56 | $211.95 |
| FFIV | 3 | $430.59 | $421.58 | $1,264.74 | $-27.03 | $388.22 |
| FTNT | 5 | $155.14 | $164.48 | $822.40 | $46.72 | $150.16 |
| HUM | 2 | $401.64 | $407.58 | $815.17 | $11.89 | $366.83 |
| IBKR | 10 | $95.61 | $97.38 | $973.80 | $17.74 | $87.64 |
| NTAP | 5 | $161.48 | $162.13 | $810.67 | $3.29 | $145.92 |
| SPY | 5 | $743.10 | $754.77 | $3,773.85 | $58.35 | — |
| STT | 8 | $185.86 | $186.71 | $1,493.68 | $6.81 | $168.04 |
| UNH | 3 | $425.21 | $418.26 | $1,254.78 | $-20.84 | $382.79 |
| URI | 1 | $1,090.35 | $1,047.94 | $1,047.94 | $-42.41 | $980.79 |

## Realized gains & tax

_No realized gains yet._

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-14T18:42` no_trade skip_entry — no entry slots (positions 10/15, new today 2/2)
- `2026-07-14T16:47` no_trade — no signals crossed action thresholds this hour
- `2026-07-14T16:47` no_trade skip_entry — no entry slots (positions 10/15, new today 2/2)
- `2026-07-14T15:09` entry buy **UNH** — momentum entry: rank 10, mom 0.387, vol 26%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
