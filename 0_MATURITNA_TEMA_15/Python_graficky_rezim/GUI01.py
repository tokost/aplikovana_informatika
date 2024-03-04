# Radio button, Check button, Combobox a list box

from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

# radio button
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="male", variable=v0, value=1)
r2 = Radiobutton(window, text="female", variable=v0, value=2)
r1.place(x=100, y=50)
r2.place(x=180, y=50)

# check bitton
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text="Cricket", variable=v1)
C2 = Checkbutton(window, text="Tennis", variable=v2)
C1.place(x=100, y=100)
C2.place(x=180, y=100)

# combo box
var = StringVar()
var.set("one")
data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=60, y=150)

# list box
lb = Listbox(window, height=5, selectmode="multiple")
for num in data:
    lb.insert(END, num)
lb.place(x=250, y=150)

# text field
txtfld = Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=65, y=200)

# button
btn = Button(window, text="This is Button widget", fg="blue")
btn.place(x=70, y=230)
lbl = Label(window, text="This is Label widget", fg="red", font=("Helvetica", 16))
lbl.place(x=50, y=20)

window.title("Hello Python")
window.geometry("400x300+10+10")
window.mainloop()
