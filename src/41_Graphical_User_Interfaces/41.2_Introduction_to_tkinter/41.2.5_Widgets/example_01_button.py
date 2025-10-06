#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.ok = tkinter.Button(self)
        self.ok["text"] = "label"
        self.ok["command"] = self.handler
        self.ok.pack()
        
    def handler(self):
        print("Button pressed")


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("200x100")
    app = MyApp(root)
    app.mainloop()
