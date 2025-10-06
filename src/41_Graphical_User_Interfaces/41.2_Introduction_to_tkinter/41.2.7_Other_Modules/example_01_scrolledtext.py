#!/usr/bin/env python

import tkinter
import tkinter.scrolledtext


class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.text = tkinter.scrolledtext.ScrolledText(master)
        self.text.pack()
        self.text.insert("end", """In the section about the text widget we said that it is possible to provide a text widget with a vertical scrollbar via the yscrollcommand option. However, since such a vertical scrollbar is usually desired for a text widget, it would be cumbersome to have to write the code to instantiate and bind the scrollbar each time.
For this purpose, the module scrolledtext exists in the package tkinter, which provides the widget ScrolledText. This widget behaves like a text widget, but comes with a vertical scrollbar by default, so the programmer doesn't have to worry about it anymore.""")


if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyApp(root)
    app.mainloop()
