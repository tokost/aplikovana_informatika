import tkinter

# Create the main window
window = tkinter.Tk()
window.geometry("300x200")
window.title("PythonExamples.org")

canvas = tkinter.Canvas()
canvas.pack()

x = [20, 10, 30, 50, 60, 70]
canvas.create_polygon(x)

window.mainloop()

