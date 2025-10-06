#!/usr/bin/env python

from concurrent import futures
import sys
import time


def approximate_pi(n):
    pi_half = 1
    numerator, denominator = 2.0, 1.0
    for i in range(n):
        pi_half *= numerator / denominator
        if i % 2:
            numerator += 2
        else:
            denominator += 2
    return 2*pi_half


if __name__ == "__main__":
    start = time.perf_counter()
    N = (34567890, 5432198, 44444444, 22222222, 56565656, 43236653, 23545353, 32425262)

    if sys.argv[1] == "threads":
        with futures.ThreadPoolExecutor(max_workers=4) as e:
            res = e.map(approximate_pi, N)
    elif sys.argv[1] == "processes":
        with futures.ProcessPoolExecutor(max_workers=4) as e:
            res = e.map(approximate_pi, N)
    else:
        res = map(approximate_pi, N)

    print(list(res))
    print(time.perf_counter() - start)
