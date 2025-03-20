# from tkinter import *

# root = Tk()
# lbl=Label(root, text="python", font=("Serif", "20"))    #using font as tuple
# lbl.pack()
# root.mainloop()


from tkinter import *
import tkinter.font as font

root = Tk()
font = font.Font(family="Serif", size=18, weight="bold")    #CREATING FONT OBJECT
lbl = Label(root, text="Programming Hero", font=font)
lbl.pack()

root.mainloop()