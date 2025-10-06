#!/usr/bin/env python

class Fibonacci:
    def __init__(self, max_n):
        self.max_n = max_n
        self.n = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max_n:
            self.n += 1
            self.a, self.b = self.b, self.a + self.b
            return self.a
        else:
            raise StopIteration


class GoldenRatio(Fibonacci):
    def __next__(self):
        super().__next__()
        return self.b / self.a


if __name__ == "__main__":
    for g in GoldenRatio(14):
        print("{:.6f}".format(g), end=" ")
    print()


