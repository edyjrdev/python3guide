#!/usr/bin/env python

import time
import random
import functools

def with_timing(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            e = time.perf_counter()
            print(f"Runtime of {fn.__name__}: {e - t}s")
    return wrapper


@with_timing
def small_nap():
    time.sleep(random.randint(1, 3))

@with_timing
def precise_nap(n):
    time.sleep(n)

@with_timing
def power_nap(stay_awake=False):
   if not stay_awake:
        time.sleep(0.1)


if __name__ == "__main__":
    small_nap()
    precise_nap(1)
    power_nap(stay_awake=True)
