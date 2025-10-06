#!/usr/bin/env python

import threading

class PrimeNumberThread(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        i = 2
        while i*i <= self.number:
            if self.number % i == 0:
                print(f"{self.number} is no prime "
                     f"as {self.number} = {i} * {self.number // i}")
                return
            i += 1
        print(f"{self.number} is prime")


if __name__ == "__main__":
    my_threads = []
    user_input = input("> ")
    while input != "e":
        try:
            thread = PrimeNumberThread(int(user_input))
            my_threads.append(thread)
            thread.start()
        except ValueError:
            print("Wrong input!")
        user_input = input("> ")
    for t in my_threads:
        t.join()



