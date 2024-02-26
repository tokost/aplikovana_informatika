

Objekt (ktorý je konkrétna reprezentácia triedy) v OOP so sebou nesie dve dôležité informácie. Prvou z týchto informácii je stav alebo vlastnosti objektu. Pomocou objektov v OOP vieme uchovávať stav a vlastnosti objektu ktorý sa môže s časom meniť. Stav resp. vlastnosti objektu si môžeme predstaviť aj tak, že na objekte definujeme nejaké údaje (čísla alebo nejaké premenné) ktoré jeho stav resp. vlastnosti reprezentujú. Tieto údaje t.j. čísla alebo premenné nazývame **atribútmi objektu**. Tieto premenné môžu byť v našom príklade napr. počet izieb a my vieme s týmito premennými manipulovať a meniť ich. 

STAV resp. VLASTNOSŤ OBJEKTU JE JEDINEČNÝM PARAMETROM KTORÝ PRISLÚCHA K TOMU DANÉMU OBJEKTU. To znamená že keď napr. zmeníme počet okien v našej obývačke v našom jednom dome, tak tento stav a vlastnosť sa zmení iba práve v tom jednom našom dome. Znamená to to, že sa zmení hodnota premennej ktorá reprezentuje počet okien v obývačke avšak tento atribút sa nezmení v ostatných domoch ktoré sme postavili pomocou daného projektu alebo triedy. 

Trieda definuje ten stav ale hodnota
tohto stavu je spojená s objektom. Takto stav objektu definujeme pomocou nejakých premenných ktoré sú naviazané na ten daný objekt.

Druhou veľmi dôležitou súčasťou objektu je jeho správanie. Správanie definujeme v časti triedy objektu avšak reálne ho vieme použiť až nad daným objektom. Pre zjednodušenie celej problematiky si predstavme že stav a správanie sa viažu iba k danému objektu. 

Spomenuli sme že stav resp. vlastnosti objektu definujeme pomocou **atribútov** premenných a ako potom definujeme to správanie ? Správanie definujeme pomocou funkcii . V počítačovom slengu povedané správanie definujeme pomocou metód resp. funkcii triedy. Takto je potom pod pojmom objekt môžeme predstaviť celok určitého dátového typu, ktorý pozostáva z atribútov premenných a funkcii.


**Definícia triedy** sa označuje kľúčovým slovíčkom **class** za ktorým nasleduje pomenovanie triedy a dvojbodka. Názov triedy pozostáva z veľkého písmena na začiatku za ktorými nasledujú písmená malé  tzv. Camel Case výrazy (t.j. pri viaclovných názvoch každé slovo začína veľkým písmenom za ktorým nasledujú malé písmená s tým, že sa nepoužíva potržník). Za názvom triedy nasleduje nový riadok a odsadenie pomocou tabulátora. Potom nasleduje tzv. telo triedy.

Podtržík sa ale používa pri tzv. Snake Case výrazoch ktoré sú používané napr. pri názvoch premenných v triede a tiež v názvoch metód správania v triede. 

**Telo triedy** pozostáva väčšinou z jednej hlavnej metódy, ktorú nazývame **konštruktor** a ktorú definujeme pomocou klúčového slovíčka **def** a názvu __init__. Táto definícia zo sebou ešte nesie niekoľko parametrov z ktorých ten prvý sa zvykne nazývať **self** a je povinný. Self je veľmi dôležitým parametrom lebo pomocou neho pristupujeme k inštancii objektu a self takto reprezentuje objekt triedy. 

To znamená že ak v konštruktore zadáme na prvom parametre self, tak pripravujem pre každý atribút ktorý nasleduje za self vnútornú premennú ktorá zodpovedá príslušnému atribútu. Takto vytvárame pomocou konštruktora objekt ktorý síce ešte fyzicky neexistuje ale už s jeho reprezentáciami v podobe vnútorných premenných s ním môžeme v tele triedy  narábať. 



~~~
# Priklad definicie triedy. Prakticky ale zbytocnej triedy 
# lebo nepouziva atributy a uloha by sa dala naprogramovat
# jednoduchsie bez pouzitia triedy. Ide vsak o nazornost

class Person:
    name = "Michal"
    def print_name():
        print(f"Meno je {Person.name}")

Person.print_name()

# Trieda je nejaky predpis, sablona, vzor niecoho. A v tomto pripade
# je to predpis osoby kedy kazda osoba ma meno a priezvisko

class Person:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
    
    def introduce_yourself(self):
        print(f"Hi I am {self.name} {self.surname}")

michal = Person("Michal", "Hucko")
michal.introduce_yourself()
katka = Person("Katka", "Huckova")
katka.introduce_yourself()

# Volanie metody v konstruktore 

class Person:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname
        self.introduce_yourself()
    
    def introduce_yourself(self):
        print(f"Hi I am {self.name} {self.surname}")

michal = Person("Michal", "Hucko")
katka = Person("Katka", "Huckova")

# Co je to ten self ? Je to univerzalne oznacenie vnutornej premennej
# v pythone. Zoberme si nasledujucu triedu

class Classroom:
    def __init__(self, student_number):
        self.student_number = student_number
    
    def get_info(self):
        print(f"Cislo studenta je {self.student_number}")

new_class = Classroom(10)
new_class.get_info() # sa vnutorne prepise na 
Classroom.get_info(new_class)

# !!!! Self v pripade prveho parametru funkcie sa nemusi volat self 
# ale moze byt pouzite akekolvek meno. Vacsinou sa vsak pouziva self

class Classroom2:
    def __init__(self, student_number):
        self.student_number = student_number
    
    def get_info(another_self):
        print(f"Cislo studenta je {another_self.student_number}")

new_class = Classroom2(20)
new_class.get_info() # sa vnutorne prepise na 

~~~