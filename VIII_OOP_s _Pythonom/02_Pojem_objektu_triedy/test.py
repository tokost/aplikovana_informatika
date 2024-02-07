https://pythontutor.com/render.html#mode=display

# Trieda je nejaky predpis, sablona, vzor niecoho. A v tomto pripade
# je to predpis ktory sa tyka osoby a ktory hovori ze osoba ma meno a priezvisko

class Person:
    def __init__(self, name, surname, vek):
        self.name = name
        self.surname = surname
        self.vek = vek
        
    def introduce_yourself(self):
        print(f"Ja som {self.name} {self.surname} mam {self.surname} rokov")


michal = Person("Michal", "Hucko", "70")
michal.introduce_yourself()

katka = Person("Katka", "Huckova", "55")
katka.introduce_yourself()
