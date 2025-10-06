#!/usr/bin/env python

from struct import unpack

with open("coffee.bmp", "rb") as f:
    f.seek(18)
    values = unpack("iiHH", f.read(12))
    print("Width:", values[0], "px")
    print("Height:", values[1], "px")
    print("Color depth:", values[3], "bpp")
