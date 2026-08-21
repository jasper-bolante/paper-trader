# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-21 20:52 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,655.53** |
| Total return since inception | -1.72% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,604.23 (3.02%) |
| Positions value | $17,319.74 |
| Settled cash | $2,331.21 |
| Unsettled cash (T+1) | $12.95 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.79% | 2.84% |
| Annualized volatility | 12.26% | 13.01% |
| Sharpe (rf 4%) | -1.43 | 1.45 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 33 | 33 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.34 | $737.52 | $-26.09 | $25.00 |
| BBY | 14 | $88.05 | $85.99 | $1,203.86 | $-28.89 | $80.33 |
| CRL | 2 | $285.12 | $295.37 | $590.73 | $20.49 | $265.83 |
| CSX | 17 | $50.29 | $51.59 | $877.12 | $22.16 | $46.44 |
| EXPE | 2 | $331.47 | $321.67 | $643.34 | $-19.60 | $298.17 |
| FDS | 2 | $299.76 | $299.58 | $599.16 | $-0.37 | $269.64 |
| IQV | 2 | $255.46 | $260.04 | $520.08 | $9.17 | $234.04 |
| MPC | 3 | $306.56 | $360.60 | $1,081.79 | $162.11 | $330.10 |
| NTAP | 5 | $161.48 | $192.29 | $961.45 | $154.07 | $186.39 |
| PANW | 2 | $388.17 | $357.90 | $715.80 | $-60.54 | $322.11 |
| PSX | 5 | $215.50 | $242.88 | $1,214.40 | $136.92 | $219.13 |
| SPY | 5 | $743.10 | $765.55 | $3,827.75 | $112.25 | — |
| STT | 8 | $185.86 | $187.21 | $1,497.68 | $10.81 | $173.64 |
| VEEV | 3 | $250.82 | $248.01 | $744.03 | $-8.44 | $225.63 |
| VLO | 3 | $304.72 | $348.81 | $1,046.43 | $132.27 | $315.01 |
| WST | 3 | $336.32 | $352.87 | $1,058.61 | $49.65 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-21T20:52` system — corporate_actions_synced
- `2026-08-21T19:49` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T19:49` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T19:07` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T19:07` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T17:58` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T17:03` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T17:03` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T16:00` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T16:00` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T15:05` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T15:05` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T14:08` entry buy **FDS** — momentum entry: rank 8, mom 0.452, vol 50%
- `2026-08-21T14:08` entry buy **PANW** — momentum entry: rank 1, mom 1.067, vol 45%

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
