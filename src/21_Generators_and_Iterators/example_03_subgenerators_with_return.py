#!/usr/bin/env python

def boys():
    yield "Phillip"
    yield "Steve"
    return 2

def girls():
    yield "Ella"
    yield "Linda"
    return 2

def names(also_boys=True):
    number_of_girls = (yield from girls())
    print("{} girls".format(number_of_girls))
    if also_boys:
        number_of_boys = (yield from boys())
        print("{} boys".format(number_of_boys))


if __name__ == "__main__":
    print(list(names()))
    print(list(names(False)))
