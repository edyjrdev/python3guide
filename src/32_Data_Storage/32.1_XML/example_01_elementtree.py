#!/usr/bin/env python

import xml.etree.ElementTree as ElementTree

types = {
    "int" : int,
    "str" : str
    }

def read_element(element):
    type = element.get("type", "str")
    try:
        return types[type](element.text)
    except KeyError:
        return element.text

def load_dict(filename):
    d = {}
    tree = ElementTree.parse(filename)
    tag_dict = tree.getroot()
    for entry in tag_dict:
        tag_key = entry.find("key")
        tag_value = entry.find("value")
        d[read_element(tag_key)] = read_element(tag_value)
    return d


if __name__ == "__main__":
    print(load_dict("dict.xml"))
