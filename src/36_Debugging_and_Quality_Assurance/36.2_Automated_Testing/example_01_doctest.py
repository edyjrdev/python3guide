#!/usr/bin/env python

import doctest

def fac(n):
    """
        Calculates the factorial of an integer.

        >>> fac(5)
        120
        >>> fac(10)
        3628800
        >>> fac(20)
        2432902008176640000

        A positive integer must be passed.

        >>> fac(-1)
        Traceback (most recent call last):
            ...
        ValueError: No negative numbers!
    """
    if n < 0:
        raise ValueError("No negative numbers!")
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def fac2(n):
    """
        Calculates the factorial of an integer.

        >>> fac(1000) # doctest: +ELLIPSIS
        402387260077093773543702...000
        >>> fac("Blah") # doctest: +SKIP
        'BlahBlah'
    """
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


if __name__ == "__main__":
    doctest.testmod()


