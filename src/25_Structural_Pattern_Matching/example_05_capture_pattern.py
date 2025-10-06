#!/usr/bin/env python

values = ["Hello", [], -5, 6, 3, float("-inf"), "world", {4, 6}]
last_finite_number, last_string = None, None

for value in values:
    match value:
        case (
            int() | float() | complex() as number
        ) if abs(value) < float("inf"):
            last_finite_number = number
        case str() as string:
            last_string = string

print(f"Last finite number: {last_finite_number}")
print(f"Last string:        {last_string}")
