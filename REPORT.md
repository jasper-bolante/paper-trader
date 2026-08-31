# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-31 19:35 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,785.42** |
| Total return since inception | -1.07% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,704.62 (3.52%) |
| Positions value | $15,999.32 |
| Settled cash | $1,038.54 |
| Unsettled cash (T+1) | $2,756.82 |
| Tax reserve | $9.26 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.18% | 3.34% |
| Annualized volatility | 11.76% | 12.21% |
| Sharpe (rf 4%) | -0.97 | 1.57 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 38 | 38 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.13 | $731.64 | $-31.97 | $25.00 |
| CRL | 2 | $285.12 | $287.56 | $575.12 | $4.88 | $268.70 |
| CSX | 17 | $50.29 | $50.44 | $857.48 | $2.53 | $46.58 |
| EXPE | 2 | $331.47 | $318.13 | $636.26 | $-26.68 | $305.24 |
| FDS | 2 | $299.76 | $311.69 | $623.38 | $23.85 | $278.29 |
| FTNT | 5 | $171.82 | $171.80 | $859.00 | $-0.08 | $154.62 |
| HUM | 2 | $406.24 | $384.32 | $768.64 | $-43.83 | $357.63 |
| IQV | 2 | $255.46 | $261.12 | $522.23 | $11.32 | $235.96 |
| MPC | 3 | $306.56 | $376.14 | $1,128.42 | $208.74 | $331.92 |
| NTAP | 4 | $187.95 | $186.27 | $745.08 | $-6.71 | $174.52 |
| PSX | 5 | $215.50 | $247.96 | $1,239.78 | $162.30 | $219.69 |
| SPY | 5 | $743.10 | $766.43 | $3,832.15 | $116.65 | — |
| STT | 8 | $185.86 | $191.40 | $1,531.16 | $44.29 | $174.19 |
| TECH | 12 | $72.32 | $72.31 | $867.72 | $-0.12 | $65.08 |
| VLO | 3 | $304.72 | $360.42 | $1,081.26 | $167.10 | $317.12 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-899.35 | $0.00 | $554.53 |

Dividends received: $61.75. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-31T19:35` entry buy **TECH** — momentum entry: rank 11, mom 0.392, vol 4%
- `2026-08-31T19:35` entry buy **FTNT** — momentum entry: rank 7, mom 0.552, vol 45%
- `2026-08-31T19:35` exit sell **VEEV** — momentum rank decayed (None > 150 or ineligible: volatility 0.5791043137848686 above cap 0.5)
- `2026-08-31T19:35` exit sell **PANW** — momentum rank decayed (None > 150 or ineligible: volatility 0.55859509743112 above cap 0.5)
- `2026-08-31T19:35` exit sell **BBY** — trailing stop 10%
- `2026-08-31T19:35` system **FDS** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-31T19:35` system **CSX** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-28T23:10` system — eod_complete
- `2026-08-28T23:10` system **BAX** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-27T23:02` system — eod_complete
- `2026-08-27T23:02` system **EXPE** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-27T23:02` system — corporate_actions_synced
- `2026-08-26T21:00` system — eod_complete
- `2026-08-26T18:18` no_trade — no signals crossed action thresholds this hour
- `2026-08-26T18:18` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
