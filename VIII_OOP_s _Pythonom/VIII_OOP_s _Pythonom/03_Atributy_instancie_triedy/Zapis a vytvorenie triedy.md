
https://www.reddit.com/r/learnpython/comments/14wv1h0/what_is_the_difference_between_a_class_and_a/?rdt=49810

https://stackoverflow.com/questions/18202818/classes-vs-functions

Charakteristickým znakom objektovo orientovaného programovania je vytváranie a používanie tried. Ide o prvok kódu ktorý podobá funkciam a preto vyvstáva otázka v čom je rozdiel medzi triedami a funkciami resp. kedy použiť pri programovaní funkciu a kedy triedu.

Zoberme si príklad zápisu funkcie ktorá má vypočítať súčin dvoch čísiel (cislo1 a cislo2). Funkciu nazveme **sucin** a jej kód spolu s jej zavolaním bude vyzerať nasledovne:

~~~
def sucin(cislo1, cislo2):
    return cislo1 * cislo2

print(sucin(5, 2))
~~~

**Funkcia je blok** kódu, ktorý **vykonáva určitú úlohu**. V Pythone sa definuje pomocou kľúčového slova **def**. V uvedenom príklade kód definuje funkciu *mocnina*, ktorá berie ako vstup *císlo* a vracia druhú mocninu tohto čísla ktorého hodnota je zobrazená na obrazovke.

**Trieda je vzor** alebo plán **podľa ktorého vytvárame objekty**. Definuje vlastnosti a metódy objektu. Napríklad nasledujúci kód definuje triedu s názvom *Sucin* (pozor s veľkým **S**), ktorá má dve vlastnosti cislo1 a cislo2 a jednu metódu vysledok. Metóda *vysledok* vypočítava súčin dvoch čísiel. Určite by sme si vedeli predstaviť aj obdobný kód pre výpočet plochy pri ktorom by sme nasledovne nahradili jednotlivé názvy 
Sucin -> Obdlznik, cislo1-> width, cislo2->heigh a vysledok->plocha

~~~
class Sucin:
    def __init__(self, cislo1, cislo2):
        self.cislo1 = cislo1
        self.cislo2 = cislo2

    def vysledok(self):
        return self.cislo1 * self.cislo2

    def delenie(self)
        return self.cislo1 / self.cislo2

sucin = Sucin(5, 2)
print(sucin.vysledok())

delenie = Sucin(10, 2)
print(delenie.delenie())
~~~

Hlavný rozdiel medzi funkciou a triedou je v tom, že **funkcia je opakovane použiteľný blok kódu**, zatiaľ čo **trieda je vzor na vytváranie objektov**. Funkcie sa zvyčajne používajú na vykonávanie špecifických úloh, zatiaľ čo triedy sa používajú na vytváranie objektov, ktoré majú vlastnosti a metódy.

Kedy by ste teda mali použiť funkciu a kedy triedu? Tu je niekoľko všeobecných doporučení:

* Funkciu použite vtedy, keď potrebujete vykonať iba špecifickú úlohu, ktorá nemusí byť spojená s objektom.

* Triedu použite vtedy, keď potrebujete vytvoriť a zoskúpiť objekty, ktoré májú spoločné vlastnosti a metódy.

* Triedy by ste mali používať iba vtedy, ak máte viac ako 1 funkciu a ak má zmysel udržiavať vnútorný stav atribútov (self.meno_atributu). V opačnom prípade, ak chcete iba viac krát použiť nejaké funkcie, jednoducho vytvorte modul v podobe nového súboru s príponou .py.
~~~
Príklad číslo 1:

class A(object):
    def __init__(self, ...):
        #initialize
    def a_single_method(self, ...):
        #do stuff

A-čko nie je v skutočnosti trieda, je to iba (komplikovaná) funkcia. Legitímna trieda by mala mať vždy aspoň dve metódy (bez uvažovania __init__).
~~~
~~~
Príklad číslo 2 je iba časť kódu:

class Person(object):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def compute(self, other):   
        """ Example of bad class design, don't care about the result """ 
        return self.arg1 + self.arg2 % other # %--> modulo t.j. vrati zvysok delenia

def compute(arg1, arg2, other):
     return arg1 + arg2 % other

Triedy poskytujú spôsob, ako zlúčiť niektoré údaje a súvisiace operácie. Ak robíte s údajmi iba jednu operáciu, potom použitím funkcie a odovzdaním údajov ako argumentov získate ekvivalentné správanie s menej zložitým kódom.
~~~

* Trieda je v podstate spôsob zoskupovania funkcií (t.j. metód) a údajov (t.j. vlastností) do logickej jednotky, ktorá sa týka určitého objetu alebo vecí. Ak toto zoskupovanie nepotrebujete, nie je potrebné vytvárať triedu.

* Ak máme v tele triedy zapúždrenú iba jednu funkciu tak je táto konštrukcia menej čitateľnou a menej efektívnou a preto je vhodnejšie použiť riešenie pomocou funkcie. 

Tu je jasný príklad, kedy použiť funkciu a kedy použiť triedum

Povedzme, že chcete napísať program, ktorý **vypočíta** faktoriál čísla. Použili by sme funkciu, pretože na jednorázový výpočet číselnej hodnoty faktoriálu nepotrebujeme vytvárať objekt a zaoberať sa  vlastnosťami a metódami čísla.

Povedzme, že chcete ale napísať program, ktorý **bude spravovať** zoznam kontaktov. Tu by bolo vhodné použiť triedu, pretože potrebujete vytvoriť objekty, ktoré reprezentujú každý kontakt. Trieda by nám umožnila definovať vlastnosti na evidovanie mena kontaktu, e-mailovej adresy a telefónneho čísla. Trieda by nám tiež umožnila vytvoriť metódy na pridávanie, odstraňovanie a aktualizáciu kontaktov. 

Povedzme ale že, že potrebujeme funkciu, ktorá vypočíta vek osoby s ohľadom na jej rok narodenia a aktuálny rok. Máme pre to vytvoriť triedu alebo funkciu ? Alebo to rozhodnutie  závisí od scenára čo chcem dosiahnúť ?

Závisí to od scenára. Ak chcete vypočítať iba vek osoby, použite funkciu, pretože chcete implementovať iba jedno špecifické správanie. Ak ale už máme objekt, ktorý obsahuje dátum narodenia osoby (a prípadne ďalšie údaje), máme tým možnosť doplniť do tela triedy aj výpočet veku ako jednou z ďalších funkcii súvisiacich s objektom osoby. Preto by vtedy bolo rozumnejšie túto úlohu riešiť použitím triedy. 

V prípade že triedu Person ešte nemáte vytvorenú je to na zváženie či túto triedu vytvoriť. Tým kritériom pre rozhodnutie by malo byť zodpovedanie otázky či plánujete opakovane používať koncepciou s Person veľmi často ? Ak áno, mali by ste triedu vytvoriť Person. 

Z uvedeného vyplýva že vždy sa musíte spýtať len sami seba: „Postará sa iný program o polia resp. údaje s ktorými uvažujem pri rozšírovaní triedy ?" Odpoveď na túto otázku potom určí, či rozšírite pôvodnú triedu alebo si vytvoríte niečo podobné čo naplní vaše potreby.