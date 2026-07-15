# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-15 15:09 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,050.65** |
| Total return since inception | 0.25% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,240.88 (1.20%) |
| Positions value | $16,817.58 |
| Settled cash | $3,222.70 |
| Unsettled cash (T+1) | $14.65 |
| Tax reserve | $4.28 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | 0.64% | 1.03% |
| Annualized volatility | 3.63% | 11.60% |
| Sharpe (rf 4%) | 10.04 | 5.25 |
| Max drawdown | 0.03% | 0.77% |
| EOD observations | 5 | 5 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BEN | 42 | $33.14 | $33.98 | $1,427.37 | $35.41 | $29.82 |
| CNC | 13 | $66.94 | $66.78 | $868.14 | $-2.10 | $61.84 |
| CSCO | 8 | $120.26 | $112.04 | $896.32 | $-65.77 | $109.12 |
| DVA | 6 | $227.39 | $226.96 | $1,361.76 | $-2.60 | $211.95 |
| FFIV | 3 | $430.59 | $422.08 | $1,266.25 | $-25.52 | $388.22 |
| FTNT | 5 | $155.14 | $164.21 | $821.05 | $45.37 | $150.16 |
| HUM | 2 | $401.64 | $409.80 | $819.60 | $16.32 | $365.89 |
| IBKR | 10 | $95.61 | $97.10 | $971.00 | $14.94 | $86.05 |
| NTAP | 5 | $161.48 | $161.39 | $806.95 | $-0.43 | $145.25 |
| SPY | 5 | $743.10 | $754.10 | $3,770.50 | $55.00 | — |
| STT | 8 | $185.86 | $185.76 | $1,486.08 | $-0.79 | $167.18 |
| UNH | 3 | $425.21 | $421.26 | $1,263.80 | $-11.82 | $382.79 |
| URI | 1 | $1,090.35 | $1,058.76 | $1,058.76 | $-31.59 | $980.79 |

## Realized gains & tax

_No realized gains yet._

Dividends received: $28.51. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-15T15:09` entry buy **STT** — momentum entry: rank 11, mom 0.388, vol 25%
- `2026-07-15T15:09` entry buy **NTAP** — momentum entry: rank 5, mom 0.600, vol 44%
- `2026-07-14T20:40` system — eod_complete
- `2026-07-14T18:42` no_trade — no signals crossed action thresholds this hour
- `2026-07-14T18:42` no_trade skip_entry — no entry slots (positions 10/15, new today 2/2)
- `2026-07-14T16:47` no_trade — no signals crossed action thresholds this hour
- `2026-07-14T16:47` no_trade skip_entry — no entry slots (positions 10/15, new today 2/2)
- `2026-07-14T15:09` entry buy **UNH** — momentum entry: rank 10, mom 0.387, vol 26%
- `2026-07-14T15:09` entry buy **IBKR** — momentum entry: rank 8, mom 0.455, vol 40%
- `2026-07-13T20:00` system — eod_complete
- `2026-07-13T20:00` system **BEN** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-13T20:00` system — corporate_actions_synced
- `2026-07-13T18:18` no_trade — no signals crossed action thresholds this hour
- `2026-07-13T18:18` no_trade skip_entry — no entry slots (positions 8/15, new today 2/2)
- `2026-07-13T16:06` entry buy **URI** — momentum entry: rank 8, mom 0.423, vol 35%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
