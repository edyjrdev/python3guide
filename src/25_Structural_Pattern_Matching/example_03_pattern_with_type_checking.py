#!/usr/bin/env python

class A:
    pass

value = 3.14
match value:
    case str():
        print(f"The string is: {value}")
    case int() | float() | complex():
        print(f"Here we have the number {value}.")
    case list():
        print(f"A list: {value}")
    case A():
        print("My class A :-)")
    case _:
        print(f"{type(value)}: {value}")
