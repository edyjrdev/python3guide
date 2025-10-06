#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(("", 50000))
    while True:
        data, addr = s.recvfrom(1024)
        print("[{}] {}".format(addr[0], data.decode()))


