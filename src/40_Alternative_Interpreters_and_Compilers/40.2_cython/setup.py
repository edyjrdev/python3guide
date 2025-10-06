#!/usr/bin/env python

from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules = cythonize("example_02_sort_cython.pyx")
)
setup(
    ext_modules = cythonize("example_03_sort_cython_2.pyx")
)
setup(
    ext_modules = cythonize("example_04_sort_cython_3.pyx")
)
setup(
    ext_modules = cythonize("example_05_sort_cython_4.pyx")
)
