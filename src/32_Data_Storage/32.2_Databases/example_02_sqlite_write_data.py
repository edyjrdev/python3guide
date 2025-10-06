#!/usr/bin/env python

import sqlite3


if __name__ == "__main__":
    con = sqlite3.connect("warehouse.db")
    cursor = con.cursor()

    for row in (
        (1, "2607871987", "Graphics card type 1", "FC", 0),
        (2, "19870109", "Processor type 13", "LPE", 57),
        (10, "06198823", "Power supply type 3", "FC", 0),
        (25, "11198703", "LED fan", "FC", 57),
        (26, "19880105", "Hard drive 10 TB", "LPE", 12)
    ):
        cursor.execute("INSERT INTO warehouse VALUES (?,?,?,?,?)", row)

    suppliers = (
        ("FC", "FiboComputing Inc.", "011235813"),
        ("LPE", "LettgenPetersErnesti", "026741337"),
        ("GC", "Golden Computers", "016180339")
    )
    cursor.executemany("INSERT INTO suppliers VALUES (?,?,?)", suppliers)

    customers = (
        (12, "James Everett", "Madison Ave New York, NY 10003"),
        (57, "Matt Aldwyn", "24 Sunset Dr, Los Angeles, CA 90048"),
        (64, "Steve Apple", "2 Podmac Str, San Jose, CA 95014")
    )
    cursor.executemany("INSERT INTO customers VALUES (?,?,?)", customers)
    con.commit()
