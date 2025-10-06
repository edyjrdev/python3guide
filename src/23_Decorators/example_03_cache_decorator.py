#!/usr/bin/env python

import time
import random
import functools

class CacheDecorator:
    def __init__(self):
        self.cache = {}
        self.func = None

    def cached_func(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
            print("Result calculated")
        else:
            print("Result loaded")
        return self.cache[args]

    def __call__(self, func):
        self.func = func
        return self.cached_func


@CacheDecorator()
def fac(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(fac(10))
    print(fac(20))
    print(fac(20))
    print(fac(10))

