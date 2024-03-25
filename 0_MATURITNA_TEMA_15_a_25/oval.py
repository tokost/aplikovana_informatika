# Import kniznice
from tkinter import *

# Vytvorenie instancie rámca tkinter-u
win= Tk()

# Definovanie rozmerov okna v ktorom bude kruh vykresleny
win.geometry("600x400")

# Vytvorenie objektu canvas t.j. plochy vo vnutri okna do ktoraej
# sa kreslia jednotlive objekty 
c= Canvas(win,width=400, height=400)

# Umiestnenie naho platno do grafickej aplikácie ( t.j do okna)
c.pack()

# Vlozenie ovalu do canvas-u
c.create_oval(60,60,210,210)

# Vykreslenie vsetkych 3-och casti a vytvori rozhranie na manipulaciu
win.mainloop()