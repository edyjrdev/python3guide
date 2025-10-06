#!/usr/bin/env python

import socket

ip = input("IP address: ")
message = input("Message: ")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(message.encode(), (ip, 50000))
