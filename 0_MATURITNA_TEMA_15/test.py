import tkinter

canvas = tkinter.Canvas()
canvas.pack()

# canvas.create_rectangle(50, 80, 200, 160)
canvas.create_line(50, 80, 200, 160, outline="red")
canvas.mainloop()