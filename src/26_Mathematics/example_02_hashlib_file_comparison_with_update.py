#!/usr/bin/env python

import hashlib

pwhash = "329670c3265b6ccd392e622733e9772f"

m = hashlib.md5(input("Your password, please: ").encode("utf-8"))
if pwhash == m.hexdigest():
    print("Access allowed")
else:
    print("Access denied")
