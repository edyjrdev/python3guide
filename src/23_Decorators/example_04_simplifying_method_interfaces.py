#!/usr/bin/env python

import functools

class Quote:
    def __init__(self):
        self.source = "Unknown"

    def quote(self, text):
        print("{}: '{}'".format(self.source, text))

    def set_source(self, source):
        self.source = source

    set_donald = functools.partialmethod(set_source, "Donald Duck")
    set_goofy = functools.partialmethod(set_source, "Goofy")


if __name__ == "__main__":
    quote = Quote()
    quote.set_donald()
    quote.quote("Quack")

