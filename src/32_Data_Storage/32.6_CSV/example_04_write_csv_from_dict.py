#!/usr/bin/env python

import csv

data = (
    {"brand": "Volvo", "model": "P245", "horsepower": "130"},
    {"brand": "Ford", "model": "Ecosport", "horsepower": "90"},
    {"brand": "Mercedes", "model": "CLK", "horsepower": "250"},
    {"brand": "Audi", "model": "A6", "horsepower": "350"}
)

with open("cars.csv", "w") as f_csv:
    writer = csv.DictWriter(f_csv, ["brand", "model", "horsepower"])
    writer.writeheader()
    writer.writerows(data)
