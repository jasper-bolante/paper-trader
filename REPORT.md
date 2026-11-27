# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-11-27 22:16 UTC · inception 2026-07-08 · drawdown state: **no_buys**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$18,867.06** |
| Total return since inception | -5.66% |
| S&P 500 benchmark (same $ , dividends reinvested) | $19,644.65 (-1.78%) |
| Positions value | $8,817.97 |
| Settled cash | $10,064.98 |
| Unsettled cash (T+1) | $0.00 |
| Tax reserve | $15.89 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -5.73% | -1.95% |
| Annualized volatility | 12.34% | 17.09% |
| Sharpe (rf 4%) | -1.47 | -0.44 |
| Max drawdown | 10.59% | 10.96% |
| EOD observations | 101 | 101 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| EL | 10 | $105.95 | $112.05 | $1,120.50 | $61.02 | $102.06 |
| RVTY | 9 | $122.75 | $151.40 | $1,362.60 | $257.88 | $149.17 |
| SPY | 5 | $743.10 | $728.35 | $3,641.75 | $-73.75 | — |
| TECH | 12 | $72.32 | $72.83 | $873.96 | $6.12 | $65.56 |
| VEEV | 4 | $305.03 | $271.51 | $1,086.06 | $-134.06 | $279.52 |
| WST | 2 | $370.69 | $366.55 | $733.10 | $-8.28 | $375.81 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,331.91 | $0.00 | $1,512.22 |

Dividends received: $105.91. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-11-25T22:40` system — eod_complete
- `2026-11-24T23:13` system — eod_complete
- `2026-11-24T01:09` system — eod_complete
- `2026-11-20T21:27` system — eod_complete
- `2026-11-19T21:43` system — eod_complete
- `2026-11-18T21:31` system — eod_complete
- `2026-11-17T21:52` system — eod_complete
- `2026-11-16T22:59` system — eod_complete
- `2026-11-14T01:24` system — eod_complete
- `2026-11-13T20:37` no_trade — no signals crossed action thresholds this hour
- `2026-11-13T20:37` no_trade skip_entry — no entries: drawdown state 'no_buys'
- `2026-11-13T20:37` system **TECH** — cash settles on pay date; 15% dividend tax reserved
- `2026-11-12T21:01` system — eod_complete
- `2026-11-12T01:58` system — eod_complete
- `2026-11-11T00:51` system — eod_complete

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
