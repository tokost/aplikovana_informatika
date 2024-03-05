import tkinter

a = tkinter.Tk()
c = tkinter.Canvas(a)
c.pack()

x = [50, 50, 80, 150, 130, 50, 250, 150]
c.create_polygon(x)

a.mainloop()
