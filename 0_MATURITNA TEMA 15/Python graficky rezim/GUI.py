from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack(side=LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack(side=LEFT)

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack(side=BOTTOM)

Label(root, text="First Name").pack()
Label(root, text="Last Name").pack()

e1 = Entry(root)
e2 = Entry(root)
e1.pack()
e2.pack()

root.mainloop()
