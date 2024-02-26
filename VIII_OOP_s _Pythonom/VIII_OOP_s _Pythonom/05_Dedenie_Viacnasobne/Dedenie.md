># Dedičnosť Pythonu - Inheritance

Dedičnosť nám umožňuje definovať triedu, ktorá zdedí všetky metódy a vlastnosti z inej triedy. Pritom rozlišujeme nadradenú - rodičovskú a podradenú triedu - dcérsku.

**Nadradená trieda** je trieda, z ktorej sa dedí, nazývaná aj základná trieda.

**Podradená trieda** je trieda, ktorá dedí z inej triedy, nazývanej aj odvodená trieda.

### Ako vytvoríme rodičovskú triedu
Každá trieda môže byť rodičovskou triedou, takže syntax je rovnaká ako pri vytváraní akejkoľvek inej triedy. Vytvor=ime triedu s názvom ***Person***, s ***firstname*** a ***lastname*** a metódou ***printname***:
~~~
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        rint(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
~~~


### Ako vytvoríme dcérsku triedu

Ak chcete vytvoriť triedu, ktorá zdedí funkčnosť z inej triedy, odošleme pri vytváraní podradenej triedy ako parameter rodičovskú triedu. Vytvoríme triedu s názvom ***Student**, ktorá zdedí vlastnosti a metódy z triedy ***Person***. Okrem toho táto trieda nič iné nevykoná a preto má iba jeden príkaz ***pass***:
~~~
class Student(Person):
    pass
~~~
**Poznámka:** Kľúčové slovo sa použite, vtedy keď do triedy nechceme pridať žiadne ďalšie vlastnosti alebo metódy.

>Teraz má trieda Študent rovnaké vlastnosti a metódy ako trieda Osoba.

Príklad:
Použite triedu ***Student*** na vytvorenie objektu a potom spustite metódu ***printname***.
~~~
x = Student("Mike", "Olsen")
x.printname()
~~~
~~~
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()
~~~

### Pridanei funkcie __init__()

Funkcia __init__()sa volá automaticky vždy, keď sa trieda použije na vytvorenie nového objektu. My sme doteraz vytvorili podradenú triedu, ktorá dedí vlastnosti a metódy od svojho rodiča. Funkciu __init__() chceme pridať do podradenej triedy (namiesto kľúčového slova pass). Keď pridáte funkciu __init__() do podradenej triedy ***Student***, podradená trieda už nebude dediť funkciu __init__() od rodiča ako to bolo v predchádzajúcom príklade.
~~~
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
~~~
**Poznámka:** Funkcia __init__() u potomka má prednosť pred dedením funkcie __init__() od rodiča. Ak ale chceme zachovať dedičnosť tejto funkcie od rodiča, pridáme volanie funkcie __init__() od rodiča do triedy Student:
~~~
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
~~~
Týmto sme úspešne pridali funkciu __init__() do triedy Student a zachovali sme aj dedičnosť nadradenej triedy Person čo nám umožňuje aby sme pridali funkcionalitu do funkcie __init__() triedy Student..

### Použitie funkcie super()

V Pythone môžeme vyššie vytvorený zámer dedenia riešiť použitím funkcie super(). Vďaka nej podriadená trieda zdedí všetky metódy a vlastnosti od svojho rodiča. Jej použitie vyzerá nasledovne:
~~~
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
~~~
Použitím funkcie super() nemusíme používať názov nadradeného prvku, ten automaticky zdedí metódy a vlastnosti od svojho rodiča.

### Pridávanie vlastností do podradenej triedy

Ak opríklad pridáme do podradenej triedy Student vlastnosť volanú graduationyear :
~~~
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
~~~
V nižšie uvedenom príklade by mal byť rok 2019 premennou a mal by byť odovzdaný triede Student pri vytváraní študentských objektov. Ak to chcete urobiť, pridajme do funkcie __init__() ďalší parameter s názvom year:
~~~
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
~~~

### Pridávanie metódy - funkcie do podradenej triedy

Ako príklad pridajme do triedy Student metódu s názvom welcome:
~~~
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
~~~
Ak pridáte metódu do podradenej triedy s rovnakým názvom ako má funkcia v nadradenej triede, dedenie nadradenej metódy bude prepísané.

[Video](https://www.youtube.com/watch?v=eERQiO9OIGw&list=PLNAMH_0HgWT_qPUxA1750M5om7iodrCtK&index=5&pp=iAQB)