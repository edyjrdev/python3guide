#!/usr/bin/env python

import threading

class PrimeNumberThread(threading.Thread):
    in_out_lock = threading.Lock()
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        i = 2
        while i*i <= self.number:
            if self.number % i == 0:
                with PrimeNumberThread.in_out_lock:
                    print(f"{self.number} is no prime "
                          f"as {self.number} = {i} * {self.number // i}")
                return
            i += 1
        with PrimeNumberThread.in_out_lock:
            print(f"{self.number} is prime")


if __name__ == "__main__":
    my_threads = []
    user_input = input("> ")
    while user_input != "e":
        try:
            thread = PrimeNumberThread(int(user_input))
            my_threads.append(thread)
            thread.start()
        except ValueError:
            with PrimeNumberThread.in_out_lock:
                print("Wrong input!")
        with PrimeNumberThread.in_out_lock:
            user_input = input("> ")
    for t in my_threads:
        t.join()


