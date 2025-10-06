#!/usr/bin/env python

import math

class Constants:
    inf = math.inf
    minf = -math.inf

value = 12345
match value:
    case int() | float() | complex() if abs(value) < Constants.inf:
        print(f"Here we have the finite number {value}.")
    case math.inf | Constants.minf:
        print("This is infinite!")
    case _:
        print(f"{type(value)}: {value}")
