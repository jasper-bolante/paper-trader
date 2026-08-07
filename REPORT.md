# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-07 16:26 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,302.27** |
| Total return since inception | -3.49% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,673.66 (3.37%) |
| Positions value | $16,644.24 |
| Settled cash | $1,218.43 |
| Unsettled cash (T+1) | $1,446.40 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -4.22% | 3.19% |
| Annualized volatility | 11.48% | 15.02% |
| Sharpe (rf 4%) | -4.79 | 2.31 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 22 | 22 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.28 | $763.84 | $0.23 | $24.54 |
| BBY | 14 | $88.05 | $81.40 | $1,139.60 | $-93.15 | $79.24 |
| CSCO | 8 | $131.57 | $121.06 | $968.52 | $-84.07 | $108.28 |
| CSX | 17 | $50.29 | $50.70 | $861.99 | $7.03 | $46.01 |
| DDOG | 3 | $268.94 | $237.10 | $711.31 | $-95.51 | $211.93 |
| FTNT | 7 | $149.43 | $159.85 | $1,118.95 | $72.91 | $151.44 |
| HPQ | 31 | $28.20 | $29.20 | $905.35 | $31.11 | $25.38 |
| MPC | 3 | $306.56 | $300.69 | $902.07 | $-17.61 | $287.83 |
| NTAP | 5 | $161.48 | $188.87 | $944.33 | $136.95 | $172.38 |
| PSX | 5 | $215.50 | $205.31 | $1,026.55 | $-50.93 | $191.32 |
| SPY | 5 | $743.10 | $771.82 | $3,859.10 | $143.60 | — |
| STT | 8 | $185.86 | $184.53 | $1,476.28 | $-10.59 | $168.31 |
| VLO | 3 | $304.72 | $300.71 | $902.13 | $-12.03 | $283.28 |
| WST | 3 | $336.32 | $354.74 | $1,064.22 | $55.26 | $316.04 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-819.48 | $0.00 | $324.57 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-07T16:26` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T16:26` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T15:29` no_trade — no signals crossed action thresholds this hour
- `2026-08-07T15:29` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-07T14:34` entry buy **CSCO** — momentum entry: rank 8, mom 0.353, vol 36%
- `2026-08-07T14:34` entry buy **BAX** — momentum entry: rank 4, mom 0.473, vol 50%
- `2026-08-07T14:34` exit sell **HUM** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-07T14:34` exit sell **DOC** — momentum rank decayed (None > 150 or ineligible: below 50DMA (trend filter))
- `2026-08-07T00:25` system — eod_complete
- `2026-08-06T16:00` entry buy **HPQ** — momentum entry: rank 5, mom 0.453, vol 44%
- `2026-08-06T16:00` entry buy **DDOG** — momentum entry: rank 1, mom 0.960, vol 46%
- `2026-08-06T15:59` exit sell **DDOG** — trailing stop 10%
- `2026-08-05T20:10` system — eod_complete
- `2026-08-05T18:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-05T18:07` no_trade skip_entry **CVS** — insufficient investable cash (size $394, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
