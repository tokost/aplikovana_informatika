import tkinter

canvas = tkinter.Canvas()
canvas.pack()

a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
canvas.create_polygon(a, b, c, d, fill="blue")
canvas.mainloop()
