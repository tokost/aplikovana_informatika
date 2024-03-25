import tkinter

canvas = tkinter.Canvas()
canvas.pack()

a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
canvas.create_line(a, b, c, d)

for bod in a, b, c, d:
    canvas.create_text(bod, text="+", fill="red")

canvas.mainloop()
