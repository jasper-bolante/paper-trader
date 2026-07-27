# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-27 16:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,472.07** |
| Total return since inception | -2.64% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,870.54 (-0.65%) |
| Positions value | $18,471.15 |
| Settled cash | $992.69 |
| Unsettled cash (T+1) | $13.89 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.41% | -0.82% |
| Annualized volatility | 9.74% | 11.33% |
| Sharpe (rf 4%) | -5.62 | -1.83 |
| Max drawdown | 3.03% | 2.21% |
| EOD observations | 13 | 13 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $63.54 | $826.02 | $-44.22 | $61.84 |
| DDOG | 3 | $260.67 | $253.66 | $761.00 | $-21.00 | $236.93 |
| DOC | 32 | $22.25 | $22.25 | $711.84 | $-0.18 | $20.02 |
| DVA | 6 | $227.39 | $236.60 | $1,419.60 | $55.24 | $213.53 |
| FTNT | 5 | $155.14 | $153.89 | $769.45 | $-6.23 | $150.16 |
| HUM | 2 | $401.64 | $381.95 | $763.90 | $-39.38 | $366.83 |
| IBKR | 10 | $95.61 | $90.67 | $906.65 | $-49.41 | $87.64 |
| JBHT | 3 | $277.72 | $277.57 | $832.72 | $-0.45 | $249.82 |
| MPC | 3 | $306.56 | $309.85 | $929.54 | $9.86 | $287.83 |
| NTAP | 5 | $161.48 | $167.75 | $838.77 | $31.39 | $151.02 |
| PSX | 5 | $215.50 | $206.49 | $1,032.45 | $-45.03 | $191.32 |
| SPY | 5 | $743.10 | $737.82 | $3,689.10 | $-26.40 | — |
| STT | 8 | $185.86 | $183.36 | $1,466.88 | $-19.99 | $168.04 |
| TRGP | 5 | $282.92 | $271.50 | $1,357.47 | $-57.13 | $256.96 |
| UNH | 3 | $425.21 | $418.33 | $1,254.99 | $-20.63 | $393.25 |
| VLO | 3 | $304.72 | $303.59 | $910.77 | $-3.39 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-323.13 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-24T19:01` no_trade skip_entry **CVS** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **JBHT** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T17:08` no_trade — no signals crossed action thresholds this hour
- `2026-07-24T17:08` no_trade skip_entry **MNST** — insufficient investable cash (size $392, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
