#!/usr/bin/env python
from struct import unpack

with open("coffee.bmp", "rb") as f:
    f.seek(18)
    width, height = unpack("ii", f.read(8))
    f.seek(2, 1)
    bpp = unpack("H", f.read(2))[0]

print("Width:", width, "px")
print("Height:", height, "px")
print("Color depth:", bpp, "bpp")
