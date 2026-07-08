"""Build data/universe.csv (S&P 500 constituents + GICS sector) from
Wikipedia. Run manually now and then to refresh the snapshot:
    python tools/build_universe.py
"""
import csv
import os
import re
import sys

import requests

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "data", "universe.csv")


def main():
    html = requests.get(URL, headers={"User-Agent": "paper-trader/1.0"},
                        timeout=30).text
    m = re.search(r'<table[^>]*id="constituents".*?</table>', html, re.S)
    if not m:
        sys.exit("could not find constituents table")
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", m.group(0), re.S)
    out = []
    for row in rows:
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)
        if len(cells) < 4:
            continue
        def clean(c):
            c = re.sub(r"<[^>]+>", "", c)
            return c.replace("&amp;", "&").strip()
        sym, name, sector = clean(cells[0]), clean(cells[1]), clean(cells[2])
        if not sym or sym == "Symbol" or not re.fullmatch(r"[A-Z]+(\.[A-Z])?", sym):
            continue
        out.append({"symbol": sym, "name": name, "sector": sector})
    if len(out) < 400:
        sys.exit(f"only parsed {len(out)} rows; page layout changed?")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["symbol", "name", "sector"])
        w.writeheader()
        w.writerows(sorted(out, key=lambda r: r["symbol"]))
    print(f"wrote {len(out)} symbols to {OUT}")


if __name__ == "__main__":
    main()
