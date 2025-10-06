#!/usr/bin/env python

import math
import trace
import sys

def program():
    for i in range(100):
        i**2
        for j in range(100):
            math.sqrt(j)
            for k in range(100):
                math.log(k+1)


if __name__ == "__main__":
    tracer = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=0)
    tracer.run("program()")
    r = tracer.results()
    r.write_results(show_missing=True, coverdir="result_tracing")
    print("Result written to result_tracing/example_03_tracing.cover")
