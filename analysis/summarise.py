"""Print mean temperature and total rainfall per site."""

import csv
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "measurements.csv"


def main():
    temps = defaultdict(list)
    rain = defaultdict(float)
    with DATA.open(newline="") as f:
        for row in csv.DictReader(f):
            temps[row["site"]].append(float(row["temperature_c"]))
            rain[row["site"]] += float(row["rainfall_mm"])

    for site in sorted(temps):
        mean = sum(temps[site]) / len(temps[site])
        print(f"{site:>6}: mean temp {mean:.1f} C, total rain {rain[site]:.1f} mm")


if __name__ == "__main__":
    main()
