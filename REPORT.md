# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-03 20:14 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,593.31** |
| Total return since inception | -2.03% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,314.08 (1.57%) |
| Positions value | $13,959.53 |
| Settled cash | $1,704.74 |
| Unsettled cash (T+1) | $3,944.69 |
| Tax reserve | $15.66 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.32% | 1.39% |
| Annualized volatility | 12.07% | 11.05% |
| Sharpe (rf 4%) | -0.87 | 0.08 |
| Max drawdown | 5.68% | 3.57% |
| EOD observations | 83 | 83 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $104.94 | $1,049.45 | $-10.03 | $98.41 |
| IT | 4 | $220.40 | $204.45 | $817.80 | $-63.79 | $184.00 |
| MPC | 2 | $442.06 | $427.37 | $854.74 | $-29.38 | $400.18 |
| NTAP | 4 | $207.54 | $189.51 | $758.06 | $-72.12 | $179.28 |
| PSX | 4 | $270.63 | $273.96 | $1,095.84 | $13.31 | $254.55 |
| RVTY | 9 | $122.75 | $167.21 | $1,504.89 | $400.17 | $149.17 |
| SPY | 5 | $743.10 | $753.88 | $3,769.38 | $53.88 | — |
| TECH | 12 | $72.32 | $72.67 | $872.10 | $4.26 | $65.44 |
| VEEV | 4 | $305.03 | $304.83 | $1,219.34 | $-0.78 | $274.35 |
| WDAY | 6 | $194.97 | $198.73 | $1,192.38 | $22.58 | $178.25 |
| WST | 2 | $370.69 | $412.78 | $825.56 | $84.18 | $374.59 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-897.76 | $0.00 | $1,363.00 |

Dividends received: $104.43. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-03T20:14` entry buy **IT** — momentum entry: rank 6, mom 0.518, vol 44%
- `2026-11-03T20:14` entry buy **VEEV** — momentum entry: rank 2, mom 0.782, vol 31%
- `2026-11-03T20:14` exit sell **IQV** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-11-03T20:14` exit sell **CRL** — momentum rank decayed (None > 150 or ineligible: volatility 0.5135575388287749 above cap 0.5)
- `2026-11-03T20:14` exit sell **IT** — trailing stop 10%
- `2026-11-03T20:14` exit sell **PLTR** — trailing stop 10%
- `2026-11-03T20:14` exit sell **APA** — trailing stop 10%
- `2026-11-02T22:26` system — eod_complete
- `2026-10-30T23:07` system — eod_complete
- `2026-10-30T23:07` system **SPY** — benchmark_dividend
- `2026-10-30T18:47` entry buy **NTAP** — momentum entry: rank 7, mom 0.614, vol 42%
- `2026-10-30T18:47` entry buy **IT** — momentum entry: rank 5, mom 0.623, vol 45%
- `2026-10-30T18:47` no_trade skip_entry **VEEV** — sector cap: Health Care would exceed 25% of equity
- `2026-10-30T18:47` exit sell **NTAP** — trailing stop 10%
- `2026-10-30T18:47` exit sell **ZBRA** — trailing stop 10%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
