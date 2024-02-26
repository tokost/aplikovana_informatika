"""
V tomto príklade vytvoríme Canvas canvas_1 a vytvoríme na tomto plátne čiaru od (10, 10) do (200,150).
Obdĺžnik na plátne od (50, 50) do (200, 150)
"""

import tkinter as tk

# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("PythonExamples.org")

# Create a Canvas widget
canvas_1 = tk.Canvas(window, width=300, height=200)
canvas_1.pack()

# Create a line on the canvas
rectangle_1 = canvas_1.create_rectangle(50, 50, 200, 150)

window.mainloop()
