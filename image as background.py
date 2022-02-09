from cProfile import label
from tkinter import *

root = Tk()
root.title("<TITLE>")
root.geometry("1015x570")
from PIL import ImageTk, Image

# canvas = Canvas(root, width = 300, height = 300)
# canvas.pack()
# img = ImageTk.PhotoImage(Image.open("ball.png"))
# canvas.create_image(20, 20, anchor=NW, image=img)
# bg(root, width = 300, height = 300)
bg = ImageTk.PhotoImage(Image.open("ball.png"))
Label1 = Label(root, image=bg)
Label1.place(x=0, y=0, relwidth=1, relheight=1)

#
tex = Label(
    root, text="B 75"
)  # set background to color of image so it look see through
tex.pack()
root.mainloop()


# bg = PhotoImage(file  = "test/images/ball.png")
# bg = PhotoImage(file  = "Folder/file")

root.mainloop()
