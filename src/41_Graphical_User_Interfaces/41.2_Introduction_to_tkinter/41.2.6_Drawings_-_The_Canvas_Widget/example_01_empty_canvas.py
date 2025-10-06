#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.cv = tkinter.Canvas(self, width=200, height=100)
        self.cv.pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("300x300")
    app = MyApp(root)
    app.mainloop()
