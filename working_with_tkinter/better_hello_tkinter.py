import tkinter as tk
from tkinter import ttk

class HelloView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello World!")
        name_label = ttk.Label(self, text="Name:")
        #store contents entry box bound to variable name instead of to widget name_entry
        name_entry = ttk.Entry(self, textvariable=self.name)
        ch_button = ttk.Button(self, text="Change", command=self.on_change)
        """
        textvariable: we can change the text by just changing the hello
        string variable
        font(font_name, font_size)
        wraplength: how wide the text can be before wrapping to the next line
        in pixels
        """
        hello_label = ttk.Label(self, textvariable=self.hello_string,
                                font=("TkDefaultFont", 64), wraplength=600)
        """
        grid allow to position widgets
        sticky: which side of the cell the contents must stick to
        add these together: nameentry to both east and west so it will
        stretch to whole column
        columnspan hello label: span three grid columns
        """
        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        ch_button.grid(row=0,column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)
        """
        weight the first column more than the others so
        this one will expand horizontally and squash surrounding c
        olumns to their min widths
        """
        self.columnconfigure(1, weight=1)
        """
        """

    def on_change(self):
        if self.name.get().strip():
            self.hello_string.set("Hello " + self.name.get())
        else:
            self.hello_string.set("Hello World")

#subclass becomes main application object could create problems
#if we want more myapplication objects
class MyApplication(tk.Tk):
    """Hello World main app"""

    def __init__(self, *args, **kwargs):
        #no parent widget
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        HelloView(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)

if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()



