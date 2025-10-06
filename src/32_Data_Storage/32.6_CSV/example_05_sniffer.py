#!/usr/bin/env python

import csv

with open("cars.csv") as f_csv:
    sample = f_csv.read(1024)
dialect = csv.Sniffer().sniff(sample)

print("Delimiter:", dialect.delimiter)
print("Has Headers:", csv.Sniffer().has_header(sample))

with open("cars.csv") as f_csv:
    reader = csv.reader(f_csv, dialect)
    for row in reader:
        print(row)

