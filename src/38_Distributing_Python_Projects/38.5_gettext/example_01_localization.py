#!/usr/bin/env python

import gettext
import random

trans = gettext.translation("myprogram", "locale", ["de"])
trans.install()
values = []

while True:
    w = input(_("Please enter a value: "))
    if not w:
        break
    values.append(w)

print(_("The random choice is {}").format(random.choice(values)))

