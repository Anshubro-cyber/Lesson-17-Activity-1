from tkinter import*

root = Tk()
root.title('image')
root.geometry('400x400')

image = tkinter.PhotoImage(file="img.jpg")

label = Label(root, image, height=350, width=300)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360)
label.pack()
label2.pack()
root.mainloop()