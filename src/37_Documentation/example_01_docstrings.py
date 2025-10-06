#!/usr/bin/env python

import math


class MyClass:
    """Example of docstrings.

    This class shows how docstrings are
    used.
    """
    pass


def MyFunction():
    """This function does nothing.

    Seriously, this function really does nothing.
    """
    pass


if __name__ == "__main__":
    print(MyClass.__doc__)
    print(MyFunction.__doc__)
    print(math.__doc__)
