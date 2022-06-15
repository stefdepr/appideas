from tkinter import *
from tkinter.ttk import *

root = Tk()
label = Label(root, text="hello world")
label.pack()
entry = Entry(root, text="write text")
entry.pack()
button = Button(root, text="click")
button.pack()

root.mainloop()
