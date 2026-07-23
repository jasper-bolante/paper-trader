# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-07-23 15:34 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,613.87** |
| Total return since inception | -1.93% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,148.03 (0.74%) |
| Positions value | $18,229.94 |
| Settled cash | $1,375.71 |
| Unsettled cash (T+1) | $13.89 |
| Tax reserve | $5.67 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.14% | 0.56% |
| Annualized volatility | 9.37% | 10.55% |
| Sharpe (rf 4%) | -3.47 | 1.01 |
| Max drawdown | 1.77% | 1.73% |
| EOD observations | 11 | 11 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| CNC | 13 | $66.94 | $63.92 | $830.96 | $-39.28 | $61.84 |
| DDOG | 3 | $260.67 | $243.45 | $730.35 | $-51.65 | $236.93 |
| DVA | 6 | $227.39 | $234.05 | $1,404.30 | $39.94 | $213.53 |
| FFIV | 3 | $430.59 | $392.32 | $1,176.97 | $-114.80 | $388.22 |
| FTNT | 5 | $155.14 | $151.79 | $758.95 | $-16.73 | $150.16 |
| HUM | 2 | $401.64 | $392.81 | $785.62 | $-17.66 | $366.83 |
| IBKR | 10 | $95.61 | $90.22 | $902.20 | $-53.86 | $87.64 |
| MPC | 3 | $306.56 | $315.74 | $947.22 | $27.54 | $287.83 |
| NTAP | 5 | $161.48 | $166.21 | $831.05 | $23.67 | $149.88 |
| PSX | 5 | $215.50 | $212.24 | $1,061.20 | $-16.28 | $191.32 |
| SPY | 5 | $743.10 | $736.13 | $3,680.65 | $-34.85 | — |
| STT | 8 | $185.86 | $184.90 | $1,479.20 | $-7.67 | $168.04 |
| TRGP | 5 | $282.92 | $288.42 | $1,442.10 | $27.49 | $255.94 |
| UNH | 3 | $425.21 | $421.35 | $1,264.05 | $-11.57 | $393.25 |
| VLO | 3 | $304.72 | $311.70 | $935.12 | $20.96 | $283.28 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-193.54 | $0.00 | $0.00 |

Dividends received: $37.83. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-07-23T15:34` no_trade — no signals crossed action thresholds this hour
- `2026-07-23T15:34` no_trade skip_entry **MNST** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **CSX** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **DOC** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **BNY** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **MGM** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **BBY** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **WST** — insufficient investable cash (size $389, need >= $500)
- `2026-07-23T15:34` no_trade skip_entry **CVS** — insufficient investable cash (size $389, need >= $500)
- `2026-07-22T20:40` system — eod_complete
- `2026-07-22T20:40` system — corporate_actions_synced
- `2026-07-22T18:43` no_trade — no signals crossed action thresholds this hour
- `2026-07-22T18:43` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-07-22T16:57` no_trade — no signals crossed action thresholds this hour
- `2026-07-22T16:57` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
