#!/usr/bin/env python

class Squares:
    def __init__(self, max_n):
        self.max_n = max_n

    def __getitem__(self, index):
        index += 1  # 0*0 is not very interesting ...
        if index > len(self) or index < 1:
            raise IndexError
        return index*index

    def __len__(self):
        return self.max_n


if __name__ == "__main__":
    print(list(Squares(20)))


