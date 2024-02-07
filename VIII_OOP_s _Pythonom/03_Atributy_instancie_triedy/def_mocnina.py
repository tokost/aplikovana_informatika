def sucin(cislo1, cislo2):
    return cislo1 * cislo2

print(sucin(5, 2))


class Sucin:
    def __init__(self, cislo1, cislo2):
        self.cislo1 = cislo1
        self.cislo2 = cislo2

    def vysledok(self):
        return self.cislo1 * self.cislo2
    
'''   def delenie(self):
        return self.cislo1 / self.cislo2 '''

sucin = Sucin(5, 3)
print(sucin.vysledok())

sucin = Sucin(5, 4)
print(sucin.vysledok())

'''
delenie = Sucin(10, 2)
print(delenie.delenie()) '''


class Obdlznik:
    def __init__(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska

    def plocha(self):
        return self.sirka * self.vyska

obdlznik = Obdlznik(5, 5)
print(obdlznik.plocha())

