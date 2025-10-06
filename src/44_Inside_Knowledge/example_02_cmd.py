#!/usr/bin/env python

import cmd
import time

class MyConsole(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "==> "
        self.start_time = None

    def do_date(self, prm):
        d = time.localtime()
        print("Today is {}-{:02}-{:02}".format(d[0],d[1],d[2]))
        return False

    def help_date(self):
        print("Outputs the current date")

    def do_time(self, prm):
        z = time.localtime()
        print("It is {:02}:{:02}:{:02}".format(z[3], z[4], z[5]))
        return False

    def do_timer(self, prm):
        if prm == "start":
            self.start_time = time.perf_counter()
        elif prm == "get":
            print("{} seconds have passed".format(int(time.perf_counter() - self.start_time)))

    def do_exit(self, prm):
        print("Goodbye")
        return True


if __name__ == "__main__":
    konsole = MyConsole()
    konsole.cmdloop()
