#!/usr/bin/env python

class A:
    def __init__(self):
        print("Constructor of A")
        self.x = 1337

    def m(self):
        print("Method m of A. It’s self.x =", self.x)


class B(A):
    def n(self):
        print("Method n of B")


if __name__ == "__main__":
    b = B()
    b.n()
    b.m()

