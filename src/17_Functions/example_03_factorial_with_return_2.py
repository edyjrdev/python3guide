#!/usr/bin/env python

def fac(number):
    if number < 0:
        return None
    result = 1
    for i in range(2, number+1):
        result *= i
    return result

while True:
    user_input = int(input("Enter a number: "))
    result = fac(user_input)
    if result is None:
        print("Error during calculation")
    else:
        print(result)
