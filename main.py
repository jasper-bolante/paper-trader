"""Entrypoint. The scheduler always runs --mode auto; the engine decides
whether this is an hourly decision cycle, the end-of-day cycle, or a no-op
(market closed)."""
import argparse
import sys

from trader import engine


def main():
    p = argparse.ArgumentParser(description="hourly paper-trading agent")
    p.add_argument("--mode", default="auto",
                   choices=["auto", "hourly", "eod", "report"])
    args = p.parse_args()
    try:
        result = engine.run(args.mode)
    except Exception as e:
        print(f"RUN FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        raise
    print(f"run complete: {result}")


if __name__ == "__main__":
    main()
