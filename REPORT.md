# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-06 16:00 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,197.35** |
| Total return since inception | -4.01% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,718.34 (3.59%) |
| Positions value | $16,255.53 |
| Settled cash | $2,263.03 |
| Unsettled cash (T+1) | $685.59 |
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
| BBY | 14 | $88.05 | $81.30 | $1,138.20 | $-94.55 | $79.24 |
| CSX | 17 | $50.29 | $50.98 | $866.75 | $11.79 | $46.01 |
| DDOG | 3 | $268.94 | $235.48 | $706.44 | $-100.38 | $211.93 |
| DOC | 32 | $22.25 | $21.26 | $680.32 | $-31.70 | $20.55 |
| FTNT | 7 | $149.43 | $160.34 | $1,122.35 | $76.31 | $151.44 |
| HPQ | 31 | $28.20 | $28.20 | $874.04 | $-0.20 | $25.38 |
| HUM | 2 | $383.80 | $357.89 | $715.78 | $-51.81 | $327.49 |
| MPC | 3 | $306.56 | $301.34 | $904.02 | $-15.66 | $287.83 |
| NTAP | 5 | $161.48 | $187.41 | $937.07 | $129.69 | $171.42 |
| PSX | 5 | $215.50 | $204.88 | $1,024.40 | $-53.08 | $191.32 |
| SPY | 5 | $743.10 | $768.08 | $3,840.40 | $124.90 | — |
| STT | 8 | $185.86 | $187.54 | $1,500.32 | $13.45 | $168.31 |
| VLO | 3 | $304.72 | $301.02 | $903.06 | $-11.10 | $283.28 |
| WST | 3 | $336.32 | $347.46 | $1,042.38 | $33.42 | $316.04 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-872.29 | $0.00 | $234.96 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-06T16:00` entry buy **HPQ** — momentum entry: rank 5, mom 0.453, vol 44%
- `2026-08-06T16:00` entry buy **DDOG** — momentum entry: rank 1, mom 0.960, vol 46%
- `2026-08-06T15:59` exit sell **DDOG** — trailing stop 10%
- `2026-08-05T20:10` system — eod_complete
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

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
