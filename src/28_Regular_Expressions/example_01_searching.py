#!/usr/bin/env python

import re

with open("rheinwerk-publishing.html", "r") as f:
    html = f.read()

it = re.finditer(r"<a .*?href=[\"\'](.*?)[\"\'].*?>(.*?)</a>", html, re.I)

for n, m in enumerate(it):
    print("#{} Name: {}, Link: {}".format(n, m.group(2), m.group(1)))

