#!/usr/bin/env python

import random

def swirl_text(text):
    lst = []
    for word in text.split():
        w = list(word[1:-1])
        random.shuffle(w)
        lst.append(word[0] + "".join(w) + word[-1])
    return " ".join(lst)
