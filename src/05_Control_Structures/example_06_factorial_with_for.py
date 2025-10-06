#!/usr/bin/env python
while True:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Negative numbers are not allowed")
        continue

    result = 1
    for i in range(2, number+1):
        result = result * i

    print("Result:", result)
