#!/usr/bin/env python

class A1:
    def __init__(self):
        self._x = 100

    def get_x(self):
        return self._x

    def set_x(self, value):
        if value < 0:
            return
        self._x = value


class A:
    def __init__(self):
        self.x = 100

    def get_x(self):
        print("Getter called")
        return self._x

    def set_x(self, value):
        print("Setter called")
        if value < 0:
            return
        self._x = value

    x = property(get_x, set_x)


if __name__ == "__main__":
    a = A1()
    print(a.get_x())
    a.set_x(300)
    print(a.get_x())
    a.set_x(-20)
    print(a.get_x())

    print()
    a = A()
    a.x = 300
    print(a.x)
    a.x = -20
    print(a.x)




