#!/usr/bin/env python

class MyLogging:
    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def entry(self, text):
        self.f.write("==>{}\n".format(text))

    def __enter__(self):
        self.f = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()


if __name__ == "__main__":
    with MyLogging("logfile.txt") as log:
        log.entry("Hello world")
        log.entry("How are you doing?")

