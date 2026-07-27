# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-27 20:06 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,517.02** |
| Total return since inception | -2.41% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,885.61 (-0.57%) |
| Positions value | $18,513.35 |
| Settled cash | $992.69 |
| Unsettled cash (T+1) | $17.14 |
| Tax reserve | $6.16 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.48% | -0.75% |
| Annualized volatility | 9.34% | 10.87% |
| Sharpe (rf 4%) | -5.59 | -1.65 |
| Max drawdown | 3.10% | 2.21% |
| EOD observations | 14 | 14 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $64.06 | $832.85 | $-37.39 | $61.84 |
| DDOG | 3 | $260.67 | $251.85 | $755.55 | $-26.45 | $236.93 |
| DOC | 32 | $22.25 | $22.51 | $720.32 | $8.30 | $20.26 |
| DVA | 6 | $227.39 | $235.59 | $1,413.51 | $49.15 | $213.53 |
| FTNT | 5 | $155.14 | $152.29 | $761.45 | $-14.23 | $150.16 |
| HUM | 2 | $401.64 | $381.11 | $762.22 | $-41.06 | $366.83 |
| IBKR | 10 | $95.61 | $92.31 | $923.10 | $-32.96 | $87.64 |
| JBHT | 3 | $277.72 | $280.84 | $842.52 | $9.35 | $252.76 |
| MPC | 3 | $306.56 | $312.23 | $936.69 | $17.01 | $287.83 |
| NTAP | 5 | $161.48 | $169.78 | $848.90 | $41.52 | $152.80 |
| PSX | 5 | $215.50 | $207.75 | $1,038.75 | $-38.73 | $191.32 |
| SPY | 5 | $743.10 | $738.85 | $3,694.25 | $-21.25 | — |
| STT | 8 | $185.86 | $184.64 | $1,477.12 | $-9.75 | $168.04 |
| TRGP | 5 | $282.92 | $267.79 | $1,338.95 | $-75.66 | $256.96 |
| UNH | 3 | $425.21 | $417.57 | $1,252.71 | $-22.91 | $393.25 |
| VLO | 3 | $304.72 | $304.82 | $914.46 | $0.30 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-323.13 | $0.00 | $0.00 |

Dividends received: $41.08. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-27T20:06` system **DOC** — cash settles on pay date; 15% dividend tax reserved
- `2026-07-27T20:06` system — corporate_actions_synced
- `2026-07-27T18:08` no_trade — no signals crossed action thresholds this hour
- `2026-07-27T18:08` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-07-27T16:00` entry buy **DOC** — momentum entry: rank 15, mom 0.307, vol 23%
- `2026-07-27T16:00` entry buy **JBHT** — momentum entry: rank 13, mom 0.319, vol 35%
- `2026-07-27T16:00` no_trade skip_entry **CVS** — sector cap: Health Care would exceed 25% of equity
- `2026-07-24T20:48` system — eod_complete
- `2026-07-24T19:01` no_trade — no signals crossed action thresholds this hour
- `2026-07-24T19:01` no_trade skip_entry **MNST** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **BBY** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **DOC** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **NUE** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **CSX** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **WST** — insufficient investable cash (size $392, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
