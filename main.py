from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gowebkit.com - Learn To Code")
root.iconbitmap("c:/gui/gowebkit.ico")
root.geometry("700x400")


def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()

root.mainloop()