# paper-trader

A live **paper-trading agent**: simulated $20,000 in real US equities at
real-time prices, one decision cycle per hour during market hours, running
unattended on GitHub Actions. No real money. See [STRATEGY.md](STRATEGY.md)
for the strategy, risk limits, and account mechanics.

## How to check performance

Open **[REPORT.md](REPORT.md)** — regenerated after every close with equity
vs. the SPY buy-and-hold benchmark, risk metrics, positions, tax summary,
and recent decisions. Every hourly decision (including decisions *not* to
trade) is in `state/decisions.jsonl`; the full ledger is `state/trader.db`
(SQLite). Every run is a git commit, so history is auditable.

## Architecture

- **Scheduler**: `.github/workflows/trade.yml` — hourly cron during market
  hours plus one end-of-day run. The script gates on Alpaca's trading
  calendar, so holidays/early closes/DST are handled; off-hours firings
  exit quietly.
- **Data**: Alpaca free market data (real-time IEX quotes and minute bars,
  SIP daily history, corporate actions, trading calendar). No brokerage
  account needed — only free API keys.
- **Execution**: custom fill simulator (spread, size/vol-scaled impact,
  realistic limit/stop semantics) against a custom ledger (T+1 settlement,
  FIFO lots, wash sales, tax reserve). Alpaca's paper-trading engine is
  deliberately *not* used: it skips dividends, mishandles splits, and
  models no slippage.
- **State**: `state/trader.db` committed back to the repo by each run.

## Deploy (one-time)

1. Create a free Alpaca account (paper is fine) and note the API key pair.
2. Create a **private** GitHub repo and push this directory.
3. Add repo secrets `ALPACA_API_KEY_ID` and `ALPACA_API_SECRET_KEY`
   (Settings → Secrets and variables → Actions), or:
   `gh secret set ALPACA_API_KEY_ID`, `gh secret set ALPACA_API_SECRET_KEY`.
4. Enable workflows if prompted (Actions tab). Trigger a first run manually:
   `gh workflow run trade -f mode=auto` (or the "Run workflow" button).

## Local commands

```sh
.venv/Scripts/python -m unittest discover -s tests   # test suite
python main.py --mode auto      # what the scheduler runs (needs env keys)
python main.py --mode report    # regenerate REPORT.md from stored state
python tools/build_universe.py  # refresh the S&P 500 snapshot
```

## Operations

- **Liquidation halt** (−15% drawdown brake): trading stops until you
  commit an empty file at `state/RESUME`. The next run resets the
  high-water mark to current equity and resumes.
- **Changing risk parameters**: edit `config.yaml`, commit. Takes effect
  next run. Document why in the commit message — future-you is the
  audience for this experiment.
- **Failures**: a failed run leaves state untouched (single transaction
  per cycle) and shows up red in the Actions tab; the next hourly run
  picks up where it left off.
