#!/usr/bin/env python

import re

regexp = {
    "Name": r"([A-Za-z]+)\s([A-Za-z]+)",
    "Addr": r"([A-Za-z]+)\s(\d+)\s*(\d{5})\s([A-Za-z]+)",
    "P": r"(\+\d{1,3})\s(\d{3})\s(\d{3})\s(\d{4,})"
}


def read_file(filename):
    d = {}
    with open(filename) as f:
        for line in f:
            if ":" in line:
                key, d[key] = (s.strip() for s in line.split(":",1))
            elif "key" in locals():
                d[key] += "\n{}".format(line.strip())
    return d


def analyze_data(data, regexp):
    for key in data:
        if key not in regexp:
            return False
        m = re.match(regexp[key], data[key])
        if not m:
            return False
        data[key] = m.groups()
    return True


if __name__ == "__main__":
    data = read_file("id.txt")
    if analyze_data(data, regexp):
        print(data)
    else:
        print("The data is incorrect")
