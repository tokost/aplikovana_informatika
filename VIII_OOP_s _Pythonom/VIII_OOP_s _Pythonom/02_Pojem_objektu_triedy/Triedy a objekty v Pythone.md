
https://pynative.com/python-classes-and-objects/

## Triedy a objekty v Pythone


Python je objektovo orientovaný programovací jazyk. To znamená, že takmer celý kód je implementovaný pomocou špeciálnej konštrukcie nazývanej triedy. Trieda je šablóna kódu na vytváranie objektov.

Tu sa dozvieme čo je trieda a objekty v Pythone, čo sú to atribúty a metódy triedy, ako vytvárať a prístup k vlastnostiam objektu a ako upraviť resp.odstráňiť objekt.

<u>Obsah</u>\

Čo je trieda a objekty v Pythone ?\
Ako vytvoriť triedu v Pythone ?\
Ako vytvoriť objekt triedy ?\
Čo sú to atribúty triedy ?\
Čo sú to metódy tried ?\ 
Čo je to konvencia pomenovania tried ?\
prejsť Vyhlásenie v triede ?\
Čo sú to vlastnosti objektu ?\
Ako upravíme vlastnosti objektu ?\
Ako odstráňime vlastnosti objektu ?\
Ako odstráňime objekt ?\


### <u>Čo je trieda a objekty v Pythone?</u>

**Trieda** : Trieda je užívateľom definovaná dátová štruktúra, ktorá spája dátové členy a metódy do jednej jednotky. 

>Tieda čiže angl. class je plán alebo šablóna kódu na vytváranie objektov . 

Pomocou triedy môžete vytvoriť toľko objektov, koľko chcete.

**objekt** : Objekt je inštanciou triedy . Je to súbor atribútov (premenných) a metód. Na vykonávanie akcií používame objekt triedy.

**Objekty majú** dve charakteristiky: Majú **stavy a správanie** (objekt má k nemu pripojené atribúty a metódy) **Atribúty predstavujú jeho stav** a **metódy reprezentujú jeho správanie**. Pomocou jeho metód môžeme modifikovať jeho stav.

Stručne povedané, každý objekt má nasledujúcu vlastnosť.

**Identitu** : Každý objekt musí byť jednoznačne identifikovaný t.j. pomenovaný.

**Stav** : Objekt má atribúty t.j. charakteristickévlastnosti, ktoré predstavujú stav objektu a tiež odrážajú vlastnosťi objektu.

**Správanie** : Objekt má metódy alebo funkcie, ktoré reprezentujú jeho správanie.

Python je objektovo orientovaný programovací jazyk, takže všetko v Pythone sa považuje za objekt. Objekt je reálna entita. Ide o zhromažďovanie rôznych údajov a funkcií, ktoré s týmito údajmi fungujú.

Napríklad, ak navrhujeme triedu založenú na stavoch a správaní osoby "Person", potom stavy môžu byť reprezentované ako [premenné inštancie](https://pynative.com/python-instance-variables/) a správanie ako metódy inštancie triedy.

![](/obrazky/triada01.png)


![]()

~~~
Reálny príklad triedy a objektov.

Trieda : Osoba

Vlastnosti : meno, pohlavie, povolanie
Správanie : Práca, štúdium

Pomocou vyššie uvedenej triedy môžeme vytvoriť viacero objektov, ktoré zobrazujú rôzne stavy a správanie.

Objekt 1 : Jessa

Vlastnosti :
Meno: Jessa
Pohlavie: Žena
Profesia: softvérový inžinier

Správanie :
Práca: Pracuje ako softvérová vývojárka v spoločnosti ABC
Štúdium: Učí sa 2 hodiny denne

Objekt 2 : Jon

Vlastnosti :
Meno: Jon
Pohlavie muž
Profesia: Lekár

Správanie :
Práca: Pracuje ako lekár
Štúdium: Učí sa 5 hodín denne

Ako môžete vidieť, Jessa je žena a pracuje ako softvérová inžinierka. Na druhej strane, Jon je muž a je právnik. Tu sú oba objekty vytvorené z rovnakej triedy, ale majú odlišné stavy a správanie .
~~~


### <u>Ako vytvoriť triedu v Pythone ?</u>

V Pythone je trieda definovaná pomocou kľúčového slova **class**. Syntax na vytvorenie triedy je uvedená nižšie.
~~~
Syntax

class class_name:
    '''This is a docstring. I have created a new class'''
    <statement 1>
    <statement 2>
    .
    .
    <statement N>
~~~

**class_name**: Je to názov triedy\
**Docstring**: Je to prvý reťazec vo vnútri v tzv. tele triedy a obsahuje krátky popis triedy. Aj keď to nie je povinné, dôrazne sa to odporúča.\
**statements**: Atribúty a metódy triedy\

Príklad: Definujte triedu v Pythone

V tomto príklade vytvárame triedu osoby s premennými inštancie mena, pohlavia a povolania.
~~~
class Person:
    def __init__(self, name, sex, profession):
        # Vlastnosti (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession

    # Spravanie (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Spravanie (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)
~~~

### <u>Ako vytvoriť objekt triedy ?</u>

Objekt je nevyhnutný na prácu s atribútmi triedy. 

**Objekt je vytvorený pomocou názvu triedy**. 

Keď vytvoríme objekt triedy, nazýva sa to **inštancia**. Objekt sa tiež nazýva inštancia triedy.

**Konštruktor je špeciálna metóda** používaná na vytvorenie a inicializáciu objektu triedy. Táto metóda je definovaná v triede.

V Pythone je vytváranie objektov rozdelené na dve časti na [inicializáciu](https://pynative.com/python-constructors/)  objektov a vytváranie objektov. Môžeme to urobiť dvomi spôsobmi:

* Interne pomocou metódy __new__ , ktorá vytvára objekt
* A pomocou metódy __init__() môžeme implementovať konštruktor na inicializáciu objektu.
Viac o kon+struktoroch sa dozvieme v dokumente: [Konštruktory v Pythone](https://pynative.com/python-constructors/)
~~~
Syntax

<object-name> = <class-name>(<arguments>) 
~~~ 
Nižšie je uvedený kód na vytvorenie objektu triedy Osoba
~~~
jessa = Person('Jessa', 'Female', 'Software Engineer')
~~~
Kompletný príklad aj s vytvorením objektu bude:

~~~
class Person:
    def __init__(self, name, sex, profession):
        # Vlastnosti (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession

    # Spravanie (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Spravanie (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)

# Vytvorenie objektu triedy
jessa = Person('Jessa', 'Female', 'Software Engineer')

# Volanie metod
jessa.show()
jessa.work()
 Bežať

Výsledok :

Meno: Jessa 
Pohlavie: Žena 
Profesia: Softwarová inžinierka
Jessa pracuje ako softvérový inžinier
~~~

### <u>Atribúty triedy</u>

Keď navrhujeme triedu, používame premenné inštancie a premenné triedy.

V triede možno atribúty definovať do dvoch častí:

**Premenné inštancie** : Premenné inštancie sú atribúty pripojené k inštancii triedy. Premenné inštancie definujeme v konštruktore (__init__()ktorý je špecialnou metóda triedy).

**Premenné triedy** : Premenná triedy je premenná, ktorá je deklarovaná vo vnútri triedy, ale mimo akejkoľvek inštancie metódy alebo __init__() metódy.

A[]()

Objekty nezdieľajú atribúty inštancie. Namiesto toho má každý objekt svoju kópiu atribútu inštancie a je jedinečný pre každý objekt.

Všetky inštancie triedy zdieľajú premenné triedy. Na rozdiel od premenných inštancií sa však hodnota premennej triedy nemení od objektu k objektu.

Vytvorí sa iba jedna kópia statickej premennej a bude zdieľaná medzi všetkými objektmi triedy.

### <u>Prístup k vlastnostiam a priraďovanie hodnôt</u>

Atribút inštancie je možné získať alebo upraviť pomocou bodkovej notácie: 

~~~
instance_name.attribute_name.
~~~

Premenná triedy je prístupná alebo upravená pomocou názvu triedy napr.
~~~
class Student:
    # premenna triedy
    school_name = 'ABC School'

    # konstruktor
    def __init__(self, name, age):
        # premenne instancie
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
# pristup k premennej instancie
print('Student:', s1.name, s1.age)

# pristup k premennej triedy
print('School name:', Student.school_name)

# modifikacia premennej instancie
s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)

# modifikacia premennej triedy
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)


Výsledok je :

Študent: Harry 12
Názov školy: ABC School

Študent: Jessa 14
Názov školy: XYZ School
~~~

Triedne metódy
V  objektovo orientovanom programovaní , Inside a Class, môžeme definovať nasledujúce tri typy metód.

Metóda inštancie : Používa sa na prístup alebo úpravu stavu objektu. vo vnútri metódypoužívame  premenné inštancie , takéto metódy sa nazývajú metódy inštancie.
Metóda triedy : Používa sa na prístup alebo úpravu stavu triedy. Ak pri implementácii metódy používame iba  premenné triedy , potom by sme takýto typ metód mali deklarovať ako metódu triedy.
Statická metóda : Ide o všeobecnú užitočnú metódu, ktorá vykonáva úlohu izolovane. V rámci tejto metódy nepoužívame premennú inštancie alebo triedy, pretože táto statická metóda nemá prístup k atribútom triedy.
Metóda triedy Python verzus statická metóda verzus metóda inštancie
metóda triedy vs statická metóda vs metóda inštancie
Metódy inštancií fungujú na úrovni inštancií (úrovni objektu). Napríklad, ak máme zo študentskej triedy vytvorené dva objekty, môžu mať rôzne názvy, značky, čísla hodov atď. Pomocou metód inštancie môžeme pristupovať a upravovať premenné inštancie.

Metóda triedy je viazaná na triedu  a nie na objekt triedy. Má prístup iba k premenným triedy.

Čítať viac : Metóda triedy Python vs. statická metóda vs. metóda inštancie

Príklad : Definujte a zavolajte metódu inštancie a metódu triedy

# class methods demo
class Student:
    # class variable
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    # instance method
    def show(self):
        # access instance variables and class variables
        print('Student:', self.name, self.age, Student.school_name)

    # instance method
    def change_age(self, new_age):
        # modify instance variable
        self.age = new_age

    # class method
    @classmethod
    def modify_school_name(cls, new_name):
        # modify class variable
        cls.school_name = new_name

s1 = Student("Harry", 12)

# call instance methods
s1.show()
s1.change_age(14)

# call class method
Student.modify_school_name('XYZ School')
# call instance methods
s1.show()
 Bežať
Výkon

Študent: Harry 12 ABC School
Študent: Harry 14 XYZ School
Konvencia pomenovania tried
Konvencie pomenovania sú nevyhnutné v akomkoľvek programovacom jazyku pre lepšiu čitateľnosť. Ak dáme rozumné meno, ušetrí nám to neskôr čas a energiu. Písanie čitateľného kódu je jedným z hlavných princípov jazyka Python.

Pri rozhodovaní o názve triedy v Pythone by sme mali dodržiavať špecifické pravidlá.

Pravidlo 1: Názvy tried by sa mali riadiť konvenciou veľkých písmen CamelCase
Pravidlo 2: Triedy výnimiek by mali končiť na „ Chyba “.
Pravidlo 3: Ak je trieda volateľná (volanie triedy odniekiaľ), v takom prípade môžeme triede pomenovať ako funkciu .
Pravidlo 4: Vstavané triedy Pythonu sú zvyčajne slová s malými písmenami
passVyhlásenie v triede
V Pythone je pass nulový príkaz. Preto sa pri vykonaní príkazu pass nič nestane.

Príkaz passsa používa na to, aby bol v kóde prázdny blok, pretože prázdny kód nie je povolený v slučkách, definícii funkcie, definícii triedy. passVýsledkom príkazu teda nebude žiadna operácia (NOP). Vo všeobecnosti ho používame ako zástupný symbol, keď nevieme, aký kód napísať alebo pridať kód v budúcom vydaní.

Predpokladajme napríklad, že máme triedu, ktorá ešte nie je implementovaná, ale chceme ju implementovať v budúcnosti a nemôže mať prázdne telo, pretože tlmočník dáva chybu. Takže použite passpríkaz na zostavenie tela, ktoré nič nerobí.

Príklad

class Demo:
  pass
Vo vyššie uvedenom príklade sme definovali triedu bez tela. Aby sme sa vyhli chybám pri jej vykonávaní, pridali sme passpríkaz do tela triedy.

Vlastnosti objektu
Každý objekt má vlastnosti. Inými slovami, môžeme povedať, že vlastnosť objektu je asociácia medzi názvom a hodnotou .

Napríklad auto je objekt a jeho vlastnosti sú farba auta, strešné okno, cena, výroba, model, motor atď. Tu je farba názov a červená hodnota . Vlastnosti objektu nie sú nič iné ako premenné inštancie.

Vlastnosti objektu
Vlastnosti objektu
Upravte vlastnosti objektu
Každý objekt má s nimi spojené vlastnosti. Vlastnosti objektu môžeme nastaviť alebo upraviť po inicializácii objektu priamym volaním vlastnosti pomocou operátora bodka.

Obj.PROPERTY = value
 Bežať
Príklad

class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
obj = Fruit("Apple", "red")

# Modifying Object Properties
obj.name = "strawberry"

# calling the instance method using the object obj
obj.show()
# Output Fruit is strawberry and Color is red
 Bežať
Odstráňte vlastnosti objektu
Vlastnosť objektu môžeme odstrániť pomocou delkľúčového slova. Ak sa k nemu po jeho odstránení pokúsime dostať, zobrazí sa chyba.

class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show(self):
        print("Fruit is", self.name, "and Color is", self.color)

# creating object of the class
obj = Fruit("Apple", "red")

# Deleting Object Properties
del obj.name

# Accessing object properties after deleting
print(obj.name)
# Output: AttributeError: 'Fruit' object has no attribute 'name'
 Bežať
Ako vidíme, vo vyššie uvedenom príklade bol názov atribútu odstránený, keď sa pokúsime vytlačiť alebo získať prístup k tomuto atribútu, keď sa zobrazí chybové hlásenie.

Odstrániť objekty
V Pythone môžeme objekt odstrániť aj pomocou delkľúčového slova. Objekt môže byť čokoľvek ako, objekt triedy, list, tuple, setatď.

Syntax

del object_name
Príklad: Odstránenie objektu

class Employee:
    depatment = "IT"

    def show(self):
        print("Department is ", self.depatment)

emp = Employee()
emp.show()

# delete object
del emp

# Accessing after delete object
emp.show()
# Output : NameError: name 'emp' is not defined 
 Bežať
Vo vyššie uvedenom príklade vytvoríme objekt emptriedy Employee. Potom delsme pomocou kľúčového slova tento objekt odstránili.

