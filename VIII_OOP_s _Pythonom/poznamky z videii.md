Pr.01:

class Car:
    pass


použitie ako modul

from car import Car

Pr.02: car.py

clas Car:   # 1.
    
    make = None   # 2.
    model = None
    year = None
    color = None

    def drive(self):                  # 3.
        print("This car is driving")

    def stop(self):
        print("This car is stopped")


__init__ za nas vytvori objekty v inych programovacich jazykoch ??? vytvori objekty za nas ??? nasim objektom auta mozeme priradit jedinecne premenne 

def __init__(self, make, model, year, color):    # 4. parametre auta
    self.make = make        # 5. mozeme ich skutocne priradit ku konkretnym  
    self.model = model      # atributom kazdeho auta ale kazdemu z nich
    self.year = year        # musi predchadzat odkaz na objekt seba sameho
    self.color = color      # t.j. z atributov sa vytvoria vlastne objekty

                            # self.coror sa rovna akejkolvek farbe ktoru dostaneme
                            # ked sa to dostane ako argument self.color ktory sa rovna 
                            # color ???
Pre auto nasej triedy mame konstruktora ktoremu priradujeme argumenty ktore dostavame k atributom objektu nasho auta.Plus mame 2 metody. Jednu na jazdu a jednu na statie takze traz mozeme vytvarat nejake objekty aut.

Vratime sa k hlavnemu suboru main.py

from car import Car

car_1 = Car("Chevy", "Corvette",2021, "modra") # prve auto t.j. objekt nazveme c
                                               # a je to modry Chevy Corvette    # vyrobeny v roku 2021
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

v ramci nasej metody konstruktora potrebujeme 5 argumentov aby sme skonstruovali objekt auta, aby sme si sami vytvorili znacku, model,rok a farbu

ar_2 = Car("Ford", "Mustang",2022, "red") # druhe auto

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()

print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")



#-- main.py  --------------------------------------------------------
from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.drive()
car_2.stop()
#-- car.py  --------------------------------------------------------
class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
#------------------------------------------------------------------


Pr.03:

class Point:
    def __init__(self, x, y, z):
        self.move_to(x, y, z)

    def is_origin(self):
        return self.x == self.y == self.z == 0

    def move_to(self, x, y, z):
        self.x, self.y, self.z = x, y, z

p = Point(1, 2, 3)
print(p.x)
print(p.is_origin())

Ak sel zo vsade vynecham dostanem chybu ! Chyba hovori ze konstruktor ma 3 pozicne argumenty ale boli zadane 4 a my sme do bodkovej konvencie odovzdali iba 3 argumenty a 4 argument bol vlastny (self). Takze prvym argumentom pre kazdu metodu musi byt self ci uz chceme alebo nie. To znamena ze musime zachytit tu vlastnu vec ktora je odovzdana ako prvy argument ktorym je self

class Point:
    def __init__(x, y, z):
        self.move_to(x, y, z)

    def is_origin():
        return self.x == self.y == self.z == 0

    def move_to(x, y, z):
        self.x, self.y, self.z = x, y, z

vratime sa k povodnemu kodu kde zmenime metodu is_origin aby sme vratili id self-u. id je vstavana funkcia ktora vracia cislo ktore predstavuje na ktory
objekt v pamati ukazujete

class Point:
    def __init__(self, x, y, z):
        self.move_to(x, y, z)

    def is_origin(self):
        return id(self)

    def move_to(self, x, y, z):
        self.x, self.y, self.z = x, y, z

p = Point(1, 2, 3)

najprv zavolam p.is_origin() dostanem cislo 13...080
ak sa pozriem na 
id(p) dostanem rovnake cislo co znamena ze tato premenna p 
ktora ukazuje na instanciu mojej triedy ukazuje na rovnaky objekt
ako moja premenna self. Takze self je naozaj len premenna ktora
ukazuje na instanciu triedy t.j. objekt s ktorym momentalne pracujete

Este jedna vec, co ak vezmem self vsade v mojom kode a zmenim ho na this.
Funguje to ako predtym. Nejde o meno ale o konvenciu a v pythone sa pouziva self a musi to byt prvy argument

class Point:
    def __init__(this, x, y, z):
        self.move_to(x, y, z)

    def is_origin(this):
       return this.x == this.y == this.z == 0

    def move_to(this, x, y, z):
        this.x, this.y, this.z = x, y, z

p = Point(1, 2, 3) novy objekt
p.x
p.is_origin()

Takze ked python zavola metodu z vasej triedy prejde v skutocnej instancii tejto triedy s ktorou pracujete ako prvy argument


class Fruit:
    def __init__ (self):
        self.name = "apple" # 
        self.color = "red"

my_fruit = Fruit()

Su tu dva rozne atributy nazov a farba. Pomocou parametra self môžeme vytvorit atributy tak že za self dáme bodku a napise nazov atributu a rovnitkom to priradime hodnote rovnako ako to robime s beznými funkciami a takto môžeme ľahko pristupovať k hodnotám atribútov zadaním názvu objektu my_fruit za ktorým nasleduje nazov atribútu ktorý by sme chceli získať. Môžeme tiež jednoducho upraviť tieto atribúty zadaním my_fruit.color = "green" t.j. nie sme obmedzený na počiatočné hodnoty

my_fruit.color = "green" 
my_fruit.name = "kivi"

Neplní sa však takto ale úplný účel vytvárania tried pretože máme napr. pevne zakódované apple a red čím sme veľmi obmedzení a kedykoľvek by sme chceli vytvoriť iný druh koreňového objektu.

Lepším riešením by bolo zhromažďovanie týchto hodnôt atribútov formou parametrov funkcie __init__ 

                class Fruit:    
                    def __init__(self, *name, clr*)  # name a clr su *parametre* 
                        **self.name** = *name*    # nasim **atributom** sme pridali *parametre*
                        selg/color = *clr*    # a tak zakazdym ked vytvorime novu
                                            # instanciu ovocia (Fruit) triedy
                                            # dostaneme ine druhy argumentov 

                apple = Fruit(**"apple", "red"**) # apple a red su **argumenty** čím nie sme obmedzení napr. iba na jablká a môžeme ľahko vytvoriť banany a kiwi

                banana = Fruit(**"banana", "yelow"**)
                kiwi = Fruit(**"kiwi", "green"**)

Ale čo s metodami. V tomto príklade sme vytvorili metódu nazvanú detaily.

                    def details(**self**): 
                        print("my " + **self.name** + " is " + **self.color**)

                apple.details()

Hlavným znakom je že tejto funkcii musíme odovzdať parameter self čo  nej urobí metódu ktorú môžeme považovať za metódy súvisiace s objektami. def __init__ je tiež metóda ktorá definuje vnútorné premenné self za účelom aby 
bolo možné prenášať prostredníctvom tohto parametra údaje z metódy do metódy a a mali prístup k parametrom definovaným v konstruktore.

AJ KED OBE METODY MAJU ODLISNY OBSAH POMOCOU KLUCOVÉHO SLOVA self ZAISTUJE ZE VSETKY ATRIBÚTY SÚ PRÍSTUPNÉ VŠETKÝM METÓDAM. A POTOM MôŽEME TIETO METÓDY JEDNODUCHO ZAVOLAŤ ZADANÍM NÁZVU OBJEKTU ZA KTORÝM NASLEDUJE NÁZOV METÓDY.

Časté chyby:

class Fruit:
    def __init__(self, name, clr):
        self.name = name
        self.colour = clr
        exp_date = "07.20.2021"     # zabudli sme na self v __init__
                                    # tym je to lokalna premenna a nie globalna
    def details(self):              # a nedostane sa do metody details
        print("expires on " + exp_date)

    apple = Fruit("apple", "red")
    apple.details()

    Riešenie chyby je že z exp_date urobíme self alebo riadok presunieme do def details

    __init__ je metóda kde inicializujeme všetky naše atribúty ad;vod pre+co ich inicializujeme je ten že init sa automaticky spustí bez nášho zásahu s každou novou inštanciou/objektom triedy. Takže pravdepodobne sme si vsimli že sme nemuseli opakovane volať __init__ a len sme ho raz na začiatku vytvorili.

    class my_class:
        def __init__(self):
        self.attr = []

    __init__ používa parameter self ktorý vždy predstavuje aktuálnu inštanciu triedy, takže vždy keď prejdeme z metódy do metódy stále odkazujeme na ten istý objekt. Ale keď vytvoríme novú inštanciu triedy t.j. nový objekt, tak klúčové slovo self bude mať potom úplne iný význam. Napr. self v prípade jablka predstavuje samotný objekt jablka, zatiaľ čo v prípade banánu už o jablku nič nevie a self predstavuje objekt banán.

    OOP je organizovaný súbor princípov pre vývoj SW. jednoducho pracujeme s údajmi a voláme funkcie stavu pôžičky na týchto údajoch. Spájame údaje s funkcionalitou a namiesto toho pracujeme s objektami.  

    Terminológia: 
    
    * funkcie vo vnútri triedy sa budú nazývať metódy
    * názvy premenných s prefixom self. sa budú nazývať atribúty
    * a potom keď kedykoľvek pridáme názov premennej inštancie triedy, tak už
        ju nebudeme nazývať premenná ale objekt