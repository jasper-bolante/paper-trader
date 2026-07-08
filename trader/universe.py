"""Tradable universe: a committed snapshot of S&P 500 constituents with
GICS sectors (data/universe.csv, built by tools/build_universe.py).
A static snapshot drifts a little as the index changes — acceptable for
this simulation, refresh with the tool occasionally."""
import csv
import os

from . import config


def load():
    path = os.path.join(config.ROOT, "data", "universe.csv")
    out = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sym = row["symbol"].strip().upper()
            if sym:
                out.append({"symbol": sym, "name": row.get("name", ""),
                            "sector": row.get("sector", "Unknown")})
    return out


def sector_map():
    return {u["symbol"]: u["sector"] for u in load()}
