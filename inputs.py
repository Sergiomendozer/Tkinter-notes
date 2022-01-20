from tkinter import *

root = Tk()

#e = Entry(root, width = 50, fg= "blue", bg = "red", borderwidth= 10)
e = Entry(root)
e.pack() # makes the input
e.insert(0, "Enter Your name:") # insert box tell you what it wants
e.get() # gets the input


def myClick():
    myLabel = Label(root, text = "Hello " + e.get())
    myLabel.pack()



myButton = Button(root, text = "Click to enter", command = myClick)

myButton.pack()

root.mainloop()