#!/usr/bin/env python
while True:
    number = int(input("Enter a number: "))
    result = 1

    while number > 0:
        result = result * number
        number = number - 1

    print("Result:", result)
