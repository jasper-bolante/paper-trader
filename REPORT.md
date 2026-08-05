# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-05 20:10 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,457.85** |
| Total return since inception | -2.71% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,718.34 (3.59%) |
| Positions value | $15,616.97 |
| Settled cash | $1,377.21 |
| Unsettled cash (T+1) | $2,470.47 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.78% | 3.41% |
| Annualized volatility | 10.77% | 15.35% |
| Sharpe (rf 4%) | -3.61 | 2.57 |
| Max drawdown | 4.25% | 3.57% |
| EOD observations | 21 | 21 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BBY | 14 | $88.05 | $84.48 | $1,182.72 | $-50.03 | $79.24 |
| CSX | 17 | $50.29 | $51.12 | $869.12 | $14.17 | $46.01 |
| DDOG | 3 | $260.67 | $283.27 | $849.81 | $67.81 | $259.35 |
| DOC | 32 | $22.25 | $21.79 | $697.28 | $-14.74 | $20.55 |
| FTNT | 7 | $149.43 | $164.00 | $1,148.00 | $101.96 | $151.44 |
| HUM | 2 | $383.80 | $363.79 | $727.58 | $-40.01 | $327.49 |
| MPC | 3 | $306.56 | $297.61 | $892.83 | $-26.85 | $287.83 |
| NTAP | 5 | $161.48 | $186.48 | $932.40 | $125.02 | $171.42 |
| PSX | 5 | $215.50 | $202.35 | $1,011.75 | $-65.73 | $191.32 |
| SPY | 5 | $743.10 | $769.79 | $3,848.95 | $133.45 | — |
| STT | 8 | $185.86 | $187.01 | $1,496.08 | $9.21 | $168.31 |
| VLO | 3 | $304.72 | $302.32 | $906.96 | $-7.20 | $283.28 |
| WST | 3 | $336.32 | $351.16 | $1,053.48 | $44.52 | $316.04 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-872.29 | $0.00 | $134.95 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-05T18:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-05T18:07` no_trade skip_entry **CVS** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **TRV** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **NUE** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **CSCO** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **CNC** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **FFIV** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **HPQ** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T18:07` no_trade skip_entry **DVA** — insufficient investable cash (size $394, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **CVS** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **TRV** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **NUE** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **CSCO** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **CNC** — insufficient investable cash (size $395, need >= $500)
- `2026-08-05T15:41` no_trade skip_entry **FFIV** — insufficient investable cash (size $395, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
