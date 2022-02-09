# pip install pillow
from tkinter import *
from PIL import ImageTk, Image  # imports pillow

root = Tk()
root.geometry("800x500")

# call image b4 resize
original_ball = Image.open("ball.png")
# resize
resized = original_ball.resize((500, 500), Image.ANTIALIAS)
resized_ball = ImageTk.PhotoImage(resized)

# label
label = Label(root, image=resized_ball)
label.pack()

root.mainloop()
