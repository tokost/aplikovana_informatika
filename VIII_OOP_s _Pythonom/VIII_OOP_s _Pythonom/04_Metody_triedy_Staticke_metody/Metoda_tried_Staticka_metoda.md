>## Metóda tried vs statická metóda

V tejto časti sa budeme zaoberať základným rozdielom medzi metódou triedy a statickou metódou v Pythone ako aj tým kedy použiť metódu triedy a kedy použiť v pythone statickú metódu.

### Čo je metóda tried ? 

V tomto texte budeme pracovať s pojmom **dekorator** čo je funkcia, ktorá dostane iba jeden argument a vráti iba jednu hodnotu. Je však trochu speciálna lebo ako argument a tak aj návratová hodnota sú zase iné funkcie. Takýmto funkciam, ktoré operujú nad inými funkciami, hovoríme funkcie vyššieho rádu. Takže skrátene povedané, dekorátor je funkcia ktorá operuje nad inými funkciami. 

Náš dekorátor vyzerá takto **@classmethod** a je to vstavaný [dekorátor funkcií](https://www-geeksforgeeks-org.translate.goog/function-decorators-in-python-set-1-introduction/?_x_tr_sl=en&_x_tr_tl=sk&_x_tr_hl=sk&_x_tr_pto=wapp), čo je výraz, ktorý sa vyhodnotí po definovaní vašej funkcie. Výsledok tohto hodnotenia prekryje vašu definíciu funkcie. Metóda triedy prijíma triedu ako implicitný prvý argument, rovnako ako metóda inštancie prijíma inštanciu. 

Syntax metódy triedy je nasledovný:
~~~
trieda C(objekt): 
    @classmethod        # odlišné označenie
    def fun(cls, arg1, arg2, ...):
       ....
fun: je funkcia, ktorú je potrebné previesť na metódu triedy,
vráti: metódu triedy pre funkciu.
~~~
* Metóda triedy je metóda, ktorá je viazaná na triedu a nie na objekt triedy.
* Majú prístup k stavu triedy, pretože vyžaduje parameter triedy, ktorý ukazuje na triedu a nie na inštanciu objektu.
* Môže upraviť stav triedy, ktorý by sa použil vo všetkých inštanciách triedy. Môže napríklad upraviť premennú triedy, ktorá bude použiteľná pre všetky inštancie.

### Čo je statická metóda

Statická metóda implicitne neprijíma prvý argument. Statická metóda je tiež metóda, ktorá je viazaná na triedu a nie na objekt triedy. Táto metóda však nemôže pristupovať alebo upravovať stav triedy. Je prítomná v triede, pretože to má zmysel lebo je aj na určité veci použitelná.

Syntax statickej metódy je nasledovný:
~~~
class C(object): 
    @staticmethod       # odlišné označenie
    def fun(arg1, arg2, ...): 
        ... 
vracia: statická metóda pre funckiu fun.
~~~

### Metóda tried vs statická metóda

Rozdiel medzi metódou Class a statickou metódou je:
* Metóda triedy berie cls ako prvý parameter, zatiaľ čo statická metóda nepotrebuje žiadne špecifické parametre.
* Metóda triedy môže pristupovať alebo upravovať stav triedy, zatiaľ čo statická metóda k nemu nemôže pristupovať ani ho upravovať.
* Vo všeobecnosti statické metódy nevedia nič o stave triedy. Sú to metódy pomocného typu, ktoré berú niektoré parametre a pracujú na týchto parametroch. Na druhej strane metódy triedy musia mať triedu ako parameter.
* Na vytvorenie metódy triedy používame @classmethod decorator v pythone a na vytvorenie statickej metódy v pythone používame @staticmethod decorator.

### Kedy použiť triedu alebo statickú metódu?
* Vo všeobecnosti používame **metódu triedy na vytvorenie továrenských metód. Továrenské metódy vracajú pre rôzne prípady použitia objekty triedy (podobné ako konštruktor) .
* Na vytváranie úžitočných-pomocných funkcií vo všeobecnosti používame statické metódy.

### Ako definovať metódu triedy a statickú metódu?
Na definovanie metódy triedy v pythone používame decorator **@classmethod** a na definovanie statickej metódy používame decorator **@staticmethod**. Aby sme to pochopili roydiel medzi nimi pozrime si to na príklade.

 Povedzme, že chceme vytvoriť triedu Person. Na vytváranie továrenských metód používame metódy tried. V nižšie uvedenom príklade používame metódu triedy na vytvorenie objektu Person od roku narodenia. Ako je vysvetlené vyššie, na vytváranie pomocných funkcií používame statické metódy. V nižšie uvedenom príklade použijeme statickú metódu na kontrolu, či je Person dospelá alebo nie. 
~~~
# class_metod.py

# Vytvorenie class metody

class MyClass:
	def __init__(self, value):
		self.value = value

	def get_value(self):
		return self.value

# Create an instance of MyClass
obj = MyClass(10)

# Call the get_value method on the instance
print(obj.get_value()) # Output: 10

# Vysledok:
# 10
~~~

~~~
# static_method.py

# Časť - Vytvorenie statickej metody
class MyClass:
	def __init__(self, value):
		self.value = value

	@staticmethod
	def get_max_value(x, y):
		return max(x, y)

# Create an instance of MyClass
obj = MyClass(10)

print(MyClass.get_max_value(20, 30))

print(obj.get_max_value(20, 30))

# Vysledok:
# 30
# 30
~~~
Kompletná implementácia bude vyzerať takto:
~~~
# class_static_method.py

# Súčasné použitie class a staic metódy

# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

# Vysledok :
# 21
# 25
# True
~~~