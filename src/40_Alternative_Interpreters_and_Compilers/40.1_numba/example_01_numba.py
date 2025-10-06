#!/usr/bin/env python

import numba
import timeit

def approximate_pi(n):
    pi_half = 1
    numerator, denominator = 2.0, 1.0
    for i in range(n):
        pi_half *= numerator / denominator
        if i % 2:
            numerator += 2
        else:
            denominator += 2
    return 2 * pi_half


@numba.jit
def approximate_pi_jit(n):
    pi_half = 1
    numerator, denominator = 2.0, 1.0
    for i in range(n):
        pi_half *= numerator / denominator
        if i % 2:
            numerator += 2
        else:
            denominator += 2
    return 2 * pi_half


@numba.njit
def approximate_pi_njit(n):
    pi_half = 1
    numerator, denominator = 2.0, 1.0
    for i in range(n):
        pi_half *= numerator / denominator
        if i % 2:
            numerator += 2
        else:
            denominator += 2
    return 2 * pi_half


if __name__ == "__main__":
    t1 = timeit.timeit("approximate_pi(1000)", globals=globals(), number=10000)
    t2 = timeit.timeit("approximate_pi_jit(1000)", setup="approximate_pi_jit(1000)", globals=globals(), number=10000)
    t3 = timeit.timeit("approximate_pi_njit(1000)", setup="approximate_pi_njit(1000)", globals=globals(), number=10000)

    print("Runtime without Numba:", t1)

    print("Runtime with Numba (jit): ", t2)
    print("Speedup:", t1/t2)

    print("Runtime with Numba (njit): ", t3)
    print("Speedup:", t1/t3)
