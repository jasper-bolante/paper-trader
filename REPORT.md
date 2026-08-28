# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-28 23:10 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,776.68** |
| Total return since inception | -1.12% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,704.62 (3.52%) |
| Positions value | $17,009.19 |
| Settled cash | $2,761.86 |
| Unsettled cash (T+1) | $14.19 |
| Tax reserve | $8.56 |

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
| BAX | 28 | $27.27 | $26.12 | $731.36 | $-32.25 | $25.00 |
| BBY | 14 | $88.05 | $82.44 | $1,154.16 | $-78.59 | $80.33 |
| CRL | 2 | $285.12 | $291.74 | $583.48 | $13.24 | $268.70 |
| CSX | 17 | $50.29 | $51.28 | $871.76 | $16.81 | $46.58 |
| EXPE | 2 | $331.47 | $329.35 | $658.69 | $-4.25 | $305.24 |
| FDS | 2 | $299.76 | $309.21 | $618.43 | $18.90 | $278.29 |
| HUM | 2 | $406.24 | $385.64 | $771.28 | $-41.19 | $357.63 |
| IQV | 2 | $255.46 | $261.54 | $523.08 | $12.17 | $235.96 |
| MPC | 3 | $306.56 | $368.80 | $1,106.40 | $186.72 | $331.92 |
| NTAP | 4 | $187.95 | $186.97 | $747.86 | $-3.93 | $174.52 |
| PANW | 2 | $388.17 | $371.53 | $743.06 | $-33.28 | $344.44 |
| PSX | 5 | $215.50 | $244.09 | $1,220.47 | $142.99 | $219.69 |
| SPY | 5 | $743.10 | $769.28 | $3,846.40 | $130.90 | — |
| STT | 8 | $185.86 | $193.28 | $1,546.24 | $59.37 | $174.19 |
| VEEV | 3 | $250.82 | $276.48 | $829.44 | $76.97 | $253.96 |
| VLO | 3 | $304.72 | $352.36 | $1,057.08 | $142.92 | $317.12 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-879.32 | $0.00 | $554.53 |

Dividends received: $57.05. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-28T23:10` system **BAX** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-27T23:02` system — eod_complete
- `2026-08-27T23:02` system **EXPE** — cash settles on pay date; 15% dividend tax reserved
- `2026-08-27T23:02` system — corporate_actions_synced
- `2026-08-26T21:00` system — eod_complete
- `2026-08-26T18:18` no_trade — no signals crossed action thresholds this hour
- `2026-08-26T18:18` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-26T16:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-26T16:02` no_trade skip_entry — no entry slots (positions 15/15, new today 1/2)
- `2026-08-26T14:20` entry buy **HUM** — momentum entry: rank 4, mom 0.657, vol 38%
- `2026-08-26T14:20` exit sell **WST** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-25T20:57` system — eod_complete
- `2026-08-25T19:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-25T19:57` no_trade skip_entry — no entry slots (positions 15/15, new today 0/2)
- `2026-08-25T19:09` no_trade — no signals crossed action thresholds this hour

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
