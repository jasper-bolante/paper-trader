# Paper Trading Account — Performance Report

**➜ [Interactive dashboard](https://jasper-bolante.github.io/paper-trader/)** — hover/click any term to learn what it means, toggle the chart lines, and browse full trade history.

_Updated 2026-08-11 18:28 UTC · inception 2026-07-08 · drawdown state: **normal**_

![equity curve](docs/equity_curve.svg)

## Account

| | |
|---|---:|
| **Equity (net of tax reserve)** | **$19,636.36** |
| Total return since inception | -1.82% |
| S&P 500 benchmark (same $ , dividends reinvested) | $20,799.89 (4.00%) |
| Positions value | $17,840.10 |
| Settled cash | $1,043.31 |
| Unsettled cash (T+1) | $759.75 |
| Tax reserve | $6.80 |

## Risk-adjusted metrics

| Metric | Portfolio | Benchmark |
|---|---:|---:|
| Total return | -1.78% | 3.82% |
| Annualized volatility | 13.07% | 14.44% |
| Sharpe (rf 4%) | -1.75 | 2.64 |
| Max drawdown | 4.83% | 3.57% |
| EOD observations | 24 | 24 |

## Positions

| Symbol | Qty | Avg basis | Last | Value | Unrealized | Stop |
|---|---:|---:|---:|---:|---:|---:|
| BAX | 28 | $27.27 | $27.77 | $777.70 | $14.09 | $25.00 |
| BBY | 14 | $88.05 | $83.68 | $1,171.52 | $-61.23 | $79.24 |
| CSCO | 8 | $131.57 | $120.34 | $962.72 | $-89.87 | $110.34 |
| CSX | 17 | $50.29 | $50.12 | $852.04 | $-2.91 | $46.01 |
| DOC | 40 | $21.90 | $20.80 | $832.20 | $-43.87 | $18.97 |
| FTNT | 7 | $149.43 | $161.35 | $1,129.45 | $83.41 | $151.44 |
| HPQ | 31 | $28.20 | $28.81 | $893.11 | $18.87 | $27.04 |
| HUM | 2 | $398.00 | $375.61 | $751.22 | $-44.77 | $348.07 |
| MPC | 3 | $306.56 | $332.24 | $996.72 | $77.04 | $288.24 |
| NTAP | 5 | $161.48 | $196.44 | $982.22 | $174.84 | $178.85 |
| PSX | 5 | $215.50 | $222.60 | $1,113.00 | $35.52 | $193.81 |
| SPY | 5 | $743.10 | $770.07 | $3,850.33 | $134.83 | — |
| STT | 8 | $185.86 | $187.72 | $1,501.76 | $14.89 | $168.31 |
| VLO | 3 | $304.72 | $322.87 | $968.61 | $54.45 | $283.47 |
| WST | 3 | $336.32 | $352.50 | $1,057.50 | $48.54 | $318.26 |

## Realized gains & tax

| Year | ST net (allowed) | LT net (allowed) | Wash-disallowed | 
|---|---:|---:|---:|
| 2026 | $-816.00 | $0.00 | $378.72 |

Dividends received: $45.34. Assumed rates: 24% short-term, 15% long-term, 15% dividends, no state tax.

## Recent decisions

- `2026-08-11T18:28` no_trade — no signals crossed action thresholds this hour
- `2026-08-11T18:28` no_trade skip_entry **TGT** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **URI** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **NUE** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **GEN** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **UAL** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **CNC** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **DAL** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T18:28` no_trade skip_entry **FFIV** — insufficient investable cash (size $55, need >= $500)
- `2026-08-11T17:31` no_trade — no signals crossed action thresholds this hour
- `2026-08-11T17:31` no_trade skip_entry **TGT** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **URI** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **NUE** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **GEN** — insufficient investable cash (size $54, need >= $500)
- `2026-08-11T17:31` no_trade skip_entry **UAL** — insufficient investable cash (size $54, need >= $500)

_Full decision log: `state/decisions.jsonl` · full history: `state/trader.db`_
