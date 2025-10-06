#!/usr/bin/env python

import socket

ip = input("IP address: ")
with socket.create_connection((ip, 50000)) as s:
    while message := input("Message: "):
        s.send(message.encode())
        response = s.recv(1024)
        print("[{}] {}".format(ip, response.decode()))

