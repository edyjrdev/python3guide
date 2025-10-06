#!/usr/bin/env python

class SortedList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sort()

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.sort()

    def append(self, value):
        super().append(value)
        self.sort()

    def extend(self, sequence):
        super().extend(sequence)
        self.sort()

    def insert(self, index, value):
        super().insert(index, value)
        self.sort()

    def reverse(self):
        pass

    def __iadd__(self, s):
        res = super().__iadd__(s)
        self.sort()
        return res

    def __imul__(self, n):
        res = super().__imul__(n)
        self.sort()
        return res


if __name__ == "__main__":
    l = SortedList([6, 4, 3])
    print(l)
    l.append(2)
    print(l)
    l.extend([67, 0, -56])
    print(l)
    l += [100, 5]
    print(l)
    l *= 2
    print(l)







