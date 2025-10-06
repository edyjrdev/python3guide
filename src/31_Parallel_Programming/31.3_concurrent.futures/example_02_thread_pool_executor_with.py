#!/usr/bin/env python

from concurrent import futures
from time import sleep, time


def test(t):
    sleep(t)
    print(f"I have waited for {t} seconds. Time: {time():.0f}")


if __name__ == "__main__":
    print(f"Start time:                        {time():.0f}")
    with futures.ProcessPoolExecutor(max_workers=3) as e:
        e.submit(test, 9)
        e.submit(test, 2)
        e.submit(test, 5)
        e.submit(test, 6)
        print("All tasks started.")
    print("All tasks completed.")


