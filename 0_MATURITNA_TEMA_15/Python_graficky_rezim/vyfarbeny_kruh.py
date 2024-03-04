import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 190, 130
f1, f2 = "red", "blue"
for r in range(10, 130, 10):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=f1)
    f1, f2 = f2, f1
canvas.mainloop()
