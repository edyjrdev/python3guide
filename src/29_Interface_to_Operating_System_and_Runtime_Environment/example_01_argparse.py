#!/usr/bin/env python

from argparse import ArgumentParser

calc = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mult": lambda a, b: a * b,
    "div": lambda a, b: a / b
}

parser = ArgumentParser()
parser.add_argument("-o", "--operation", default="add")
parser.add_argument("op1", type=float)
parser.add_argument("op2", type=float)
args = parser.parse_args()

op = args.operation
if op in calc:
    print("Result:", calc[op](args.op1, args.op2))
else:
    parser.error("{} is not an operation".format(op))
