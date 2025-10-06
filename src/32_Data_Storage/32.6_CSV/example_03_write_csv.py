#!/usr/bin/env python

import csv

data = (
    ["Volvo", "P245", "130"],
    ["Ford", "Ecosport", "90"],
    ["Mercedes", "CLK", "250"],
    ["Audi", "A6", "350"],
)
with open("cars.csv", "w") as f_csv:
    writer = csv.writer(f_csv)
    writer.writerow(["brand", "model", "horsepower"])
    writer.writerows(data)
