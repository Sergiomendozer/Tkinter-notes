from tkinter import *


root = Tk()
root.geometry("500x500")  # size of window that opens # (left and right , up and down)

Grid.rowconfigure(root, 0, weight=1)  # 0 = row, same as
Grid.columnconfigure(root, 0, weight=1)  # 0 = column, same as


myButton = Button(root, text="click", relief="groove")
# relief = flat, groove, raised, ridge, solid, or sunken
myButton.grid(row=0, column=0, sticky="nsew")


def resize(e):
    size = e.width / 10
    myButton.config(font=("Helvetica", int(size)))


root.bind("<Configure>", resize)

root.mainloop()
