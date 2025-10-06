#!/usr/bin/env python

def fac(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    print(result)

while True:
    user_input = int(input("Enter a number: "))
    fac(user_input)
