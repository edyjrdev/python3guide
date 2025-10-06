#!/usr/bin/env python

import threading


class MyThread(threading.Thread):
    counter = 0

    def run(self):
        for i in range(2000000):
            MyThread.counter += 1


if __name__ == "__main__":
    A = MyThread()
    B = MyThread()
    A.start(), B.start()
    A.join(), B.join()

    print(MyThread.counter)
