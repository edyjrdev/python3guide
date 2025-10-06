#!/usr/bin/env python

import re

with open("rheinwerk-publishing.html", "r") as f:
    html = f.read()

it = re.finditer(r"""
    <a\ .*?             # Warning: Space after a requires backslash
        href=[\"\']     # Double or single quotes
                        # enclose the target of the link
                 (.*?)  # We allow any characters in the link target ...
             [\"\']
    .*?>
        (.*?)           # ... just like in the link text
    </a>
""", html, re.I | re.VERBOSE)

for n, m in enumerate(it):
    print("#{} Name: {}, Link: {}".format(n, m.group(2), m.group(1)))

