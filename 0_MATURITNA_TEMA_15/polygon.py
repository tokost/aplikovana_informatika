import tkinter

a = tkinter.Tk()
c = tkinter.Canvas(a)
c.pack()

x = [20, 10, 30, 50, 60, 70]
c.create_polygon(x)

a.mainloop()
