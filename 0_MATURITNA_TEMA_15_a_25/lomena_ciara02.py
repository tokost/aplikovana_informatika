import tkinter

canvas = tkinter.Canvas()
canvas.pack()

a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
canvas.create_line(a, b, c, d)

for bod in a, b, c, d:
    x, y = bod
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, outline="red")
canvas.mainloop()
