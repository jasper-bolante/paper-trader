# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-27 18:08 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,507.00** |
| Total return since inception | -2.46% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,870.54 (-0.65%) |
| Positions value | $18,506.08 |
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
| CNC | 13 | $66.94 | $64.47 | $838.05 | $-32.19 | $61.84 |
| DDOG | 3 | $260.67 | $255.16 | $765.50 | $-16.50 | $236.93 |
| DOC | 32 | $22.25 | $22.29 | $713.28 | $1.26 | $20.02 |
| DVA | 6 | $227.39 | $235.90 | $1,415.40 | $51.04 | $213.53 |
| FTNT | 5 | $155.14 | $153.54 | $767.70 | $-7.98 | $150.16 |
| HUM | 2 | $401.64 | $385.23 | $770.46 | $-32.82 | $366.83 |
| IBKR | 10 | $95.61 | $90.92 | $909.25 | $-46.81 | $87.64 |
| JBHT | 3 | $277.72 | $279.03 | $837.09 | $3.92 | $249.82 |
| MPC | 3 | $306.56 | $310.77 | $932.31 | $12.63 | $287.83 |
| NTAP | 5 | $161.48 | $169.15 | $845.73 | $38.35 | $151.02 |
| PSX | 5 | $215.50 | $207.41 | $1,037.05 | $-40.43 | $191.32 |
| SPY | 5 | $743.10 | $737.73 | $3,688.62 | $-26.88 | — |
| STT | 8 | $185.86 | $183.25 | $1,466.04 | $-20.83 | $168.04 |
| TRGP | 5 | $282.92 | $270.87 | $1,354.35 | $-60.26 | $256.96 |
| UNH | 3 | $425.21 | $418.31 | $1,254.94 | $-20.67 | $393.25 |
| VLO | 3 | $304.72 | $303.44 | $910.32 | $-3.84 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-323.13 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

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
- `2026-07-24T19:01` no_trade skip_entry **CVS** — insufficient investable cash (size $392, need >= $500)
- `2026-07-24T19:01` no_trade skip_entry **JBHT** — insufficient investable cash (size $392, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
