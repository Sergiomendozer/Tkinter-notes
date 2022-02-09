from cProfile import label
from faulthandler import disable
from tkinter import *

root = Tk()

# Grid.rowconfigure(root, 0, weight = 1) # 0 = row, same as
# Grid.columnconfigure(root, 0, weight = 1) # 0 = column, same as

# Grid.rowconfigure(root, 1, weight = 1)
# Grid.columnconfigure(root, 1, weight = 1)


myButton = Button(root, text="click")
myButton2 = Button(root, text="click2")
myButton.grid(row=0, column=0, sticky="nsew")
myButton2.grid(row=1, column=0, sticky="nsew")


# loop to assign multiple buttons sizes
button_list = [myButton, myButton2]
row_number = 0

for button in button_list:
    Grid.rowconfigure(root, row_number, weight=1)
    row_number = +1


root.mainloop()
