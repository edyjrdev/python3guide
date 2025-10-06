#!/usr/bin/env python

from xmlrpc.server import SimpleXMLRPCServer as Server

def fac(n):
    """ Calculates the factorial of the integer n. """
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def square(n):
    """ Calculates the square of the number n. """
    return n*n


if __name__ == "__main__":
    with Server(("", 50000)) as srv:
        srv.register_function(fac)
        srv.register_function(square)
        srv.serve_forever()
