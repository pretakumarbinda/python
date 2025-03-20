# #to open image in photos
# from PIL import Image
# img = Image.open("hero.png")
# img.show() 


#use in GUI:
from tkinter import *
from PIL import ImageTk, Image
root = Tk()

lbl=Label(root, text="Hero")
img=Image.open("hero.png")
picture= ImageTk.PhotoImage(img)
python= Label(root, image=picture)

lbl.pack()
python.pack()

root.mainloop()