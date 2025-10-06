#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.mb = tkinter.Menubutton(self, text="Hello World")
        
        self.menu = tkinter.Menu(self.mb, tearoff=False)
        self.menu.add_checkbutton(label="Donald Duck")
        self.menu.add_checkbutton(label="Scrooge McDuck")
        self.menu.add_checkbutton(label="Huey, Dewey and Louie")
        
        self.mb["menu"] = self.menu
        self.mb.pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("300x60")
    app = MyApp(root)
    app.mainloop()
