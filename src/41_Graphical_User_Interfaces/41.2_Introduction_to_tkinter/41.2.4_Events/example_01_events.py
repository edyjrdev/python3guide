#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()
        self.createBindings()
        
    def createWidgets(self):
        self.label = tkinter.Label(self)
        self.label.pack()
        self.label["text"] = "Please send an event"
        
        self.entry = tkinter.Entry(self)
        self.entry.pack()
        
        self.ok = tkinter.Button(self)
        self.ok.pack()
        self.ok["text"] = "Quit"
        self.ok["command"] = self.quit
        
    def createBindings(self):
        self.entry.bind("<MouseWheel>", lambda event: self.eventMouseWheel(event.delta))
        self.entry.bind("<ButtonPress-4>", lambda event: self.eventMouseWheel(1))
        self.entry.bind("<ButtonPress-5>", lambda event: self.eventMouseWheel(-1))
        
        self.entry.bind("Duckburg", self.eventDuckburg)
        self.entry.bind("<ButtonPress-1>", self.eventMouseClick)

    def eventDuckburg(self, event):
        self.label["text"] = "You know the secret password!"

    def eventMouseClick(self, event):
        self.label["text"] = "Mouse click at position ({},{})".format(event.x, event.y)

    def eventMouseWheel(self, delta):
        print(delta)
        if delta < 0:
            self.label["text"] = "Please move the mouse wheel in the other direction."
        else:
            self.label["text"] = "Thank you very much."


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyApp(root)
    app.mainloop()
