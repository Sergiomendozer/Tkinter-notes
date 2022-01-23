from tkinter import *
root = Tk()
root.title("<TITLE>")
root.geometry("1015x570")
from PIL import ImageTk,Image
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("ball.png"))
canvas.create_image(20, 20, anchor=NW, image=img)
root.mainloop()

 
# bg = PhotoImage(file  = "test/images/ball.png")
#bg = PhotoImage(file  = "Folder/file")

root.mainloop()