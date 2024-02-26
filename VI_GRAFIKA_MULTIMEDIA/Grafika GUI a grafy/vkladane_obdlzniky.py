import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 80, 200, 160)
canvas.create_rectangle(100, 120, 250, 200, outline="red")
canvas.create_rectangle(130, 100, 280, 180, outline="blue", width=5)
canvas.create_rectangle(80, 70, 230, 150, fill="yellow")
canvas.mainloop()
