#!/usr/bin/env python
words = {
    "Germany": "Deutschland",
    "Spain": "Spanien",
    "Greece": "Griechenland"
}

with open("output.txt", "w") as fobj:
    for engl in words:
        fobj.write(f"{engl} {words[engl]}\n")

