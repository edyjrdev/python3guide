#!/usr/bin/env python

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i


def generator_with_multiple_yields():
    a = 10
    yield a
    yield a * 2
    b = 5
    yield a + b


def names(also_boys=True):
    yield "Ella"
    yield "Linda"
    if not also_boys:
        return
    yield "Phillip"
    yield "Steve"


if __name__ == "__main__":
    for i in square_generator(10):
        print(i, end=" ")
    print()

    for i in generator_with_multiple_yields():
        print(i, end=" ")
    print()

    print(list(names()))
    print(list(names(False)))
