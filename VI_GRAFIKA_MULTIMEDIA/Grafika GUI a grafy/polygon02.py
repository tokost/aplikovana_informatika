import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("PythonExamples.org")

canvas = tkinter.Canvas()
canvas.pack()
a = (100, 50)
b = (30, 150)
c = (160, 120)
d = (180, 40)
canvas.create_polygon(a, b, c, d, fill="blue")

window.mainloop()
