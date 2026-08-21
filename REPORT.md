# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-21 15:05 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,655.02** |
| Total return since inception | -1.72% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,528.06 (2.64%) |
| Positions value | $17,319.23 |
| Settled cash | $2,331.21 |
| Unsettled cash (T+1) | $12.95 |
| Tax reserve | $8.37 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -2.38% | 2.46% |
| Annualized volatility | 12.31% | 13.20% |
| Sharpe (rf 4%) | -1.85 | 1.26 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 32 | 32 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $26.46 | $741.02 | $-22.59 | $25.00 |
| BBY | 14 | $88.05 | $87.87 | $1,230.18 | $-2.57 | $80.33 |
| CRL | 2 | $285.12 | $295.38 | $590.77 | $20.53 | $262.31 |
| CSX | 17 | $50.29 | $51.19 | $870.23 | $15.28 | $46.01 |
| EXPE | 2 | $331.47 | $326.73 | $653.45 | $-9.49 | $298.17 |
| FDS | 2 | $299.76 | $300.28 | $600.56 | $1.03 | $269.64 |
| IQV | 2 | $255.46 | $259.26 | $518.52 | $7.61 | $230.53 |
| MPC | 3 | $306.56 | $360.83 | $1,082.50 | $162.82 | $330.10 |
| NTAP | 5 | $161.48 | $193.59 | $967.95 | $160.57 | $186.39 |
| PANW | 2 | $388.17 | $350.63 | $701.26 | $-75.08 | $313.89 |
| PSX | 5 | $215.50 | $241.50 | $1,207.47 | $129.99 | $219.13 |
| SPY | 5 | $743.10 | $766.20 | $3,831.00 | $115.50 | — |
| STT | 8 | $185.86 | $185.26 | $1,482.08 | $-4.79 | $173.64 |
| VEEV | 3 | $250.82 | $249.43 | $748.29 | $-4.18 | $225.63 |
| VLO | 3 | $304.72 | $345.25 | $1,035.74 | $121.58 | $315.01 |
| WST | 3 | $336.32 | $352.74 | $1,058.20 | $49.24 | $318.49 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-1,057.88 | $0.00 | $536.94 |

Dividends received: $55.81. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-21T15:05` no_trade — no signals crossed action thresholds this hour
- `2026-08-21T15:05` no_trade skip_entry — no entry slots (positions 15/15, new today 2/2)
- `2026-08-21T14:08` entry buy **FDS** — momentum entry: rank 8, mom 0.452, vol 50%
- `2026-08-21T14:08` entry buy **PANW** — momentum entry: rank 1, mom 1.067, vol 45%
- `2026-08-20T20:58` system — eod_complete
- `2026-08-20T19:57` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T19:57` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` no_trade skip_entry — no entry slots (positions 13/15, new today 2/2)
- `2026-08-20T19:11` exit sell **PANW** — trailing stop 10%
- `2026-08-20T17:58` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:58` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T17:02` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T17:02` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)
- `2026-08-20T16:01` no_trade — no signals crossed action thresholds this hour
- `2026-08-20T16:01` no_trade skip_entry — no entry slots (positions 14/15, new today 2/2)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
