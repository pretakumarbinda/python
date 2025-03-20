from tkinter import *

# Define the function to be called when the button is clicked
def enroll():
    # Change the text of the output label to "enrolled successfully"
    output["text"] = "enrolled successfully"

# Create the main window
root = Tk()

# Create a label widget with the text "Python course"
lbl = Label(root, text="Python course")

# Create a button widget with the text "Enroll Now" and link it to the enroll function
btn = Button(root, text="Enroll Now", command=enroll)

# Create an output label widget (initially empty)
output = Label(root)

# Arrange the label, button, and output label in the window
lbl.pack()
btn.pack()
output.pack()

# Run the application's main loop
root.mainloop()
