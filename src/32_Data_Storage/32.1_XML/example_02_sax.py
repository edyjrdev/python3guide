#!/usr/bin/env python

import xml.sax as sax

class DictHandler(sax.handler.ContentHandler):
    types = {
        "int" : int,
        "str" : str
        }

    def __init__(self):
        self.result = {}
        self.key = ""
        self.value = ""
        self.active = None
        self.type = None

    def startElement(self, name, attrs):
        if name == "entry":
            self.key = ""
            self.value = ""
        elif name in ("key", "value"):
            self.active = name
            try:
                self.type = self.types[attrs["type"]]
            except KeyError:
                self.type = str

    def endElement(self, name):
        if name == "entry":
            self.result[self.key] = self.type(self.value)
        elif name in ("key", "value"):
            self.active = None

    def characters(self, content):
        if self.active == "key":
            self.key += content
        elif self.active == "value":
            self.value += content



def load_dict(filename):
    handler = DictHandler()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(filename)
    return handler.result


if __name__ == "__main__":
    print(load_dict("dict.xml"))
