import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 50, 50
s, v = 100, 55
farba = "red"
canvas.create_rectangle(x, y, x + s, y + v, fill=farba)
x, y = 160, 70
canvas.create_rectangle(x, y, x + s, y + v, fill=farba)
canvas.mainloop()
