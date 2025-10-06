#!/usr/bin/env python

import example_02_sort_cython
import example_03_sort_cython_2
import example_04_sort_cython_3
import example_05_sort_cython_4
import example_01_sort_python

import timeit
import random
import array


def create_list():
    values = array.array("i", range(1000))
    random.shuffle(values)
    return values


if __name__ == "__main__":
    t_py  = min(timeit.repeat("example_01_sort_python.sort(values)", globals=globals(), setup="values = create_list()", number=1, repeat=100))
    t_cy1 = min(timeit.repeat("example_02_sort_cython.sort(values)", globals=globals(), setup="values = create_list()", number=1, repeat=100))
    t_cy2 = min(timeit.repeat("example_03_sort_cython_2.sort(values)", globals=globals(), setup="values = create_list()", number=1, repeat=100))
    t_cy3 = min(timeit.repeat("example_04_sort_cython_3.sort(values)", globals=globals(), setup="values = create_list()", number=1, repeat=100))
    t_cy4 = min(timeit.repeat("example_05_sort_cython_4.sort(values)", globals=globals(), setup="values = create_list()", number=1, repeat=100))

    print("Python:", t_py)

    print("Cython #1:", t_cy1)
    print("Speedup 1:", t_py / t_cy1)

    print("Cython #2:", t_cy2)
    print("Speedup 2:", t_py / t_cy2)

    print("Cython #3:", t_cy3)
    print("Speedup 3:", t_py / t_cy3)

    print("Cython #4:", t_cy4)
    print("Speedup 4:", t_py / t_cy4)
