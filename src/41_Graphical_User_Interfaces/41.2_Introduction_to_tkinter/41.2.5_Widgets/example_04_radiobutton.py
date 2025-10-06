#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.options = ["Berlin", "London", "Ottawa", "Paris",
                        "Rome", "Tokyo", "Washington DC"]
        
        self.city = tkinter.StringVar()
        self.city.set("Ottawa")
        
        for a in self.options:
            b = tkinter.Radiobutton(self)
            b["text"] = a
            b["value"] = a
            b["variable"] = self.city
            b["command"] = self.handler
            b.pack(anchor="w")
        
    def handler(self):
        print(self.city.get())


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyApp(root)
    app.mainloop()
