#!/usr/bin/env python

import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.text = tkinter.Text(master)
        self.text.pack()
        
        self.text.tag_config("o", foreground="orange")
        self.text.tag_config("u", underline=True)
        
        self.text.insert("end", "Hello world\n")
        self.text.insert("end", "This is a long orange text\n", "o")
        self.text.insert("end", "And here we have underlined text", "u")


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyApp(root)
    app.mainloop()
