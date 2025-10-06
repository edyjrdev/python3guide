#!/usr/bin/env python

import sqlite3

class Circle:
    def __init__(self, mx, my, r):
        self.Mx = mx
        self.My = my
        self.R = r
    def __str__(self):
        return "Circle({}, {}, {})".format(self.Mx, self.My, self.R)

def circle_adapter(k):
    return "{};{};{}".format(k.Mx, k.My, k.R)

def circle_converter(bytestring):
    mx, my, r = bytestring.split(b";")
    return Circle(float(mx), float(my), float(r))


if __name__ == "__main__":
    # Register adapters and converters
    sqlite3.register_adapter(Circle, circle_adapter)
    sqlite3.register_converter("CIRCLE", circle_converter)

    # Here a sample database is stored in memory with
    # a single-column table defined for circles
    con = sqlite3.connect(":memory:",
                            detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = con.cursor()
    cursor.execute("CREATE TABLE circle_table(k CIRCLE)")

    # Write circle to database
    circle = Circle(1, 2.5, 3)
    cursor.execute("INSERT INTO circle_table VALUES (?)", (circle,))

    # Read out circle again
    cursor.execute("SELECT * FROM circle_table")

    read_circle = cursor.fetchall()[0][0]
    print(type(read_circle))
    print(read_circle)
