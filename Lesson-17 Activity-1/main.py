from tkinter import *
from tkinter import PhotoImage
root = Tk()
root.title('image')
root.geometry('400x400')

image = PhotoImage("Pls Keep Your Footwear Outside.jpg") 
label = Label(root, image=image)
label.pack()  
label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.pack()
root.mainloop()