# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-15 18:40 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$20,034.22** |
| Total return since inception | 0.17% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,240.88 (1.20%) |
| Positions value | $16,801.15 |
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
| BEN | 42 | $33.14 | $33.72 | $1,416.24 | $24.28 | $29.82 |
| CNC | 13 | $66.94 | $66.84 | $868.92 | $-1.32 | $61.84 |
| CSCO | 8 | $120.26 | $112.11 | $896.88 | $-65.21 | $109.12 |
| DVA | 6 | $227.39 | $230.83 | $1,384.98 | $20.62 | $211.95 |
| FFIV | 3 | $430.59 | $419.99 | $1,259.97 | $-31.80 | $388.22 |
| FTNT | 5 | $155.14 | $163.86 | $819.30 | $43.62 | $150.16 |
| HUM | 2 | $401.64 | $409.75 | $819.50 | $16.22 | $365.89 |
| IBKR | 10 | $95.61 | $97.31 | $973.10 | $17.04 | $86.05 |
| NTAP | 5 | $161.48 | $158.73 | $793.65 | $-13.73 | $145.25 |
| SPY | 5 | $743.10 | $754.51 | $3,772.55 | $57.05 | — |
| STT | 8 | $185.86 | $185.41 | $1,483.28 | $-3.59 | $167.18 |
| UNH | 3 | $425.21 | $419.99 | $1,259.97 | $-15.65 | $382.79 |
| URI | 1 | $1,090.35 | $1,052.81 | $1,052.81 | $-37.54 | $980.79 |

## Realized gains & tax

_No realized gains yet._

Dividends received: $28.51. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-14T15:09` entry buy **IBKR** — momentum entry: rank 8, mom 0.455, vol 40%
- `2026-07-13T20:00` system — eod_complete
- `2026-07-13T20:00` system **BEN** — cash settles on pay date; 15% dividend tax reserved

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
