#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=True)
        self.createWidgets()

    def createWidgets(self):
        self.nameEntry = tkinter.Entry(self)
        self.nameEntry.pack(expand=True)
        
        self.name = tkinter.StringVar()
        self.name.set("Your name...")
        self.nameEntry["textvariable"] = self.name
        
        self.ok = tkinter.Button(self)
        self.ok["text"] = "Ok"
        self.ok["command"] = self.quit
        self.ok.pack(side="right", expand=True)
        
        self.rev = tkinter.Button(self)
        self.rev["text"] = "Reverse"
        self.rev["command"] = self.onReverse
        self.rev.pack(side="right", expand=True)

    def onReverse(self):
        self.name.set(self.name.get()[::-1])


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("300x150")
    app = MyApp(root)
    app.mainloop()
