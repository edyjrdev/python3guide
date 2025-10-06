#!/usr/bin/env python

from typing import List

def fly(destinations):
    print("We are flying to:", ", ".join(destinations))

def walk(destinations: List[str]):
    print("We are walking to:", ", ".join(destinations))

if __name__ == "__main__":
    fly(["Rome", "Paris", "New York"])
    fly([0, 1, 2])
    fly(4)
    walk(["Rome", "Paris", "New York"])
    walk([0, 1, 2])
    walk(4)
