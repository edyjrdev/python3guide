#!/usr/bin/env python

import timeit

def fac1(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def fac2(n):
    if n > 0:
        return fac2(n-1)*n
    else:
        return 1


if __name__ == "__main__":
    t1 = timeit.Timer("fac1(50)", globals=globals())
    t2 = timeit.Timer("fac2(50)", globals=globals())

    print("Iterative: ", t1.timeit())
    print("Recursive: ", t2.timeit())

    print("Iterative: ", min(t1.repeat(100, 10000)))
    print("Recursive: ", min(t2.repeat(100, 10000)))
