#!/usr/bin/env python

import contextlib

if __name__ == "__main__":
    stdout_redirect = False
    with open("out.txt", "w") as f_out:
        if stdout_redirect:
            context = contextlib.redirect_stdout(f_out)
        else:
            context = contextlib.nullcontext()

        with context:
            print("Screen")
            print("output")


