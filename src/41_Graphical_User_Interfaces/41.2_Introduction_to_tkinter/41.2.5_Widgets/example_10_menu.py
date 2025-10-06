#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
       
        self.menuBar = tkinter.Menu(master)
        master.config(menu=self.menuBar)
        
        self.fillMenuBar()

    def fillMenuBar(self):
        self.menuFile = tkinter.Menu(self.menuBar, tearoff=False)
        
        self.menuFile.add_command(label="Open", command=self.handler)
        self.menuFile.add_command(label="Save", command=self.handler)
        self.menuFile.add_command(label="Save As", command=self.handler)
        
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Quit", command=self.quit)
        self.menuBar.add_cascade(label="File", menu=self.menuFile)

    def handler(self):
        print("Hello World!")


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("500x150")
    app = MyApp(root)
    app.mainloop()
