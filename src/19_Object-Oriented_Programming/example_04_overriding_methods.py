#!/usr/bin/env python

class A:
    def __init__(self):
        print("Constructor of A")
        self.x = 1337

    def m(self):
        print("Method m of A. It’s self.x =", self.x)


class B(A):
    def __init__(self):
        print("Constructor of B")
        super().__init__()
        self.y = 10000
    def n(self):
        print("Method n of B. It’s self.y =", self.y)


if __name__ == "__main__":
    b = B()
    b.n()
    b.m()

