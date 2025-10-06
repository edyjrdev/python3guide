#!/usr/bin/env python

def boys():
    yield "Phillip"
    yield "Steve"

def girls():
    yield "Ella"
    yield "Linda"

def names(also_boys=True):
    yield from girls()
    if also_boys:
        yield from boys()


if __name__ == "__main__":
    print(list(names()))
    print(list(names(False)))
