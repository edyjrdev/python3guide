#!/usr/bin/env python

import multiprocessing


class PrimeNumberProcess(multiprocessing.Process):
    def __init__(self, number, in_out_lock):
        super().__init__()
        self.number = number
        self.in_out_lock = in_out_lock

    def run(self):
        i = 2
        while i * i <= self.number:
            if self.number % i == 0:
                with self.in_out_lock:
                    print(f"{self.number} ist no prime "
                          f"as {self.number} = {i} * {self.number // i}")
                return
            i += 1
        with self.in_out_lock:
            print(f"{self.number} is prime")


if __name__ == "__main__":
    my_processes = []
    in_out_lock = multiprocessing.Lock()
    user_input = input("> ")
    while user_input != "e":
        try:
            process = PrimeNumberProcess(int(user_input), in_out_lock)
            my_processes.append(process)
            process.start()
        except ValueError:
            with in_out_lock:
                print("Wrong input!")

        with in_out_lock:
            user_input = input("> ")
    for p in my_processes:
        p.join()


