from cProfile import label
from faulthandler import disable
from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root, text = "Hello World!")
    myLabel.pack()


#myButton = Button(root, text = "click", state = disable)
#myButton = Button(root, text = "click", padx=50, pady = 50, font = 32)

#fg = text color
# bg = background color (hex# color does work to choose color)
myButton = Button(root, text = "click", command = myClick, fg="Blue", bg = "red")

myButton.pack()

root.mainloop()