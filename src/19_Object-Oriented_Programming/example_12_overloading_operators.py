#!/usr/bin/env python

class Length:
    conversion = {
        "m": 1,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001,
        "km": 1000,
        "ft": 0.3048,   # feet
        "in": 0.0254,   # inch
        "mi": 1609.344  # miles
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "{:f} {}".format(self.value, self.unit)

    def __add__(self, other):
        z = self.value * self.conversion[self.unit]
        z += other.value * self.conversion[other.unit]
        z /= self.conversion[self.unit]
        return Length(z, self.unit)

    def __sub__(self, other):
        z = self.value * self.conversion[self.unit]
        z -= other.value * self.conversion [other.unit]
        z /= self.conversion[self.unit]
        return Length(z, self.unit)


if __name__ == "__main__":
    a1 = Length(5, "cm")
    a2 = Length(3, "dm")
    print(a1 + a2)
    print(a2 + a1)








