#!/usr/bin/env python

import time
import contextlib

@contextlib.contextmanager
def runtime():
    start = time.perf_counter()
    try:
        yield
    finally:
        print("Runtime: {:.2f} s".format(time.perf_counter() - start))


if __name__ == "__main__":
    with runtime():
        x = 0
        for i in range(10000000):
            x += (-1) ** i * i  # A time-consuming calculation



