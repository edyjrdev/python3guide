#!/usr/bin/env python
while True:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Negative numbers are not allowed")
        continue

    result = 1
    while number > 0:
        result = result * number
        number = number - 1

    print("Result:", result)
