#!/usr/bin/env python

import time
import random

def with_timing(fn):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            e = time.perf_counter()
            print(f"Runtime of {fn.__name__}: {e - t}s")
    return wrapper


def small_nap():
    time.sleep(random.randint(1, 3))

def precise_nap(n):
    time.sleep(n)

def power_nap(stay_awake=False):
   if not stay_awake:
        time.sleep(0.1)

small_nap = with_timing(small_nap)
precise_nap = with_timing(precise_nap)
power_nap = with_timing(power_nap)


if __name__ == "__main__":
    small_nap()
    precise_nap(1)
    power_nap(stay_awake=True)
