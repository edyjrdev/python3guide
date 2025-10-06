#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.entries = ["Berlin", "London", "Ottawa", "Paris",
                        "Rome", "Tokyo", "Washington DC"]
        self.lb = tkinter.Listbox(master)
        self.lb.insert("end", *self.entries)
        self.lb.pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyApp(root)
    app.mainloop()
