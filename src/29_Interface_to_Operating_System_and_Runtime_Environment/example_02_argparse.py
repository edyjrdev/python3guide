#!/usr/bin/env python

from argparse import ArgumentParser

calc = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mult": lambda a, b: a * b,
    "div": lambda a, b: a / b
}

parser = ArgumentParser(description = "A calculator")
parser.add_argument("-o", "--operation", default="plus", help="arithmetic operation")
parser.add_argument("operands", metavar="operand", type=float, nargs="+", help="operands")
parser.add_argument("-i", "--integer", dest="type", action="store_const", const=int, default=float, help="integer calculation")
args = parser.parse_args()

op = args.operation
if op in calc:
    result = args.type(args.operands[0])
    for z in args.operands[1:]:
        result = calc[op](result, args.type(z))
    print("Result:", result)
else:
    parser.error("{} is not a valid operation".format(op))

