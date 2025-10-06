#!/usr/bin/env python

import hashlib

with open("file1.txt", "rb") as f1, open("file2.txt", "rb") as f2:
    if hashlib.md5(f1.read()).digest() == hashlib.md5(f2.read()).digest():
        print("The files are identical")
    else:
        print("The files are different")

