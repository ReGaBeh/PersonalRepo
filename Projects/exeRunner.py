import os
from tkinter import *


def openFile():
    file = entry1.get()
    os.startfile(str(file))


def closeFile():
    file = entry1.get()
    os.system("TASKKILL /F /IM " + file)


window = Tk()
window.title(".exe Runner")
window.geometry("350x150")

Label(window, text="Enter a file directory").grid(row=1)
entry1 = Entry(window)
Button(window, text="Submit", command=openFile).grid(row=2, column=1)
Button(window, text="Close the file", command=closeFile).grid(row=3, column=1)

Label(window, text="Note: to close file the directory must").grid(row=4)
Label(window, text="still be present in the entry").grid(sticky="W", row=5)

entry1.grid(row=1, column=1)

window.mainloop()
