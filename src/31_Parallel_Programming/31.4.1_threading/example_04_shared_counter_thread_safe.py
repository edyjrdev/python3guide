#!/usr/bin/env python

import threading


class MyThread(threading.Thread):
    lock = threading.Lock()
    counter = 0

    def run(self):
        for i in range(200000):
            with MyThread.lock:
                MyThread.counter += 1


if __name__ == "__main__":
    A = MyThread()
    B = MyThread()
    A.start(), B.start()
    A.join(), B.join()

    print(MyThread.counter)
