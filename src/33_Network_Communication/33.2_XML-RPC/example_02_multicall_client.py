#!/usr/bin/env python

from xmlrpc.client import ServerProxy, MultiCall

cli = ServerProxy("http://127.0.0.1:50000")
mc = MultiCall(cli)

for i in range(10):
    mc.fac(i)
    mc.square(i)

for result in mc():
    print(result)

