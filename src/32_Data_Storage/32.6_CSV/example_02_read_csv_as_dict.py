#!/usr/bin/env python

import csv

with open("names.csv") as f_csv:
    reader = csv.DictReader(f_csv)
    for line in reader:
        print(line)
