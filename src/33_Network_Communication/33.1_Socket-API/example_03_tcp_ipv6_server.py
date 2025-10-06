#!/usr/bin/env python

import socket

with socket.create_server(("", 50000), family=socket.AF_INET6) as s:
    s.listen(1)
    while True:
        comm, addr = s.accept()
        while data := comm.recv(1024):
            print("[{}] {}".format(addr[0], data.decode()))
            message = input("Response: ")
            comm.send(message.encode())
        comm.close()
