Python základy:
* od dátový typov cez funkcie k modulom
* umožňuje 
    * funkcionálne programovanoe - implementovanie funkcii
    * procedurálne programovanie - rozdelenie kódu ma menšie časti
    * a aj OOP - 

poznať a naučiť sa princípy :
    * datové typy
    * premenné 
    * funkcie 
    * moduly

OOP je o reprezentovaní vecí v našom kóde :
    * ako reprezentovať údaje v našom kóde\
        * jednoduché údaje = základné dátové typy a kolekcie napr. uložiť císlo 5 alebo reťazec "hello" resp. nara
        * reprezentácia niečoho zložitejšieho ako napr. xml, json kde možno využiť práve OOP

OOP\
    * Abstraction   - abstrakcia\
    * Encapsulation - zapúzdrenie\
    * Inheritance   - dedičnosť\
    * Polymorphism  - [polymorfizmus](https://cs.wikipedia.org/wiki/Polymorfismus_(programov%C3%A1n%C3%AD))

Najprv však treba pochopiť čo je to objekt:

Objekt je vec z reálneho života. Môže to byť niečo fyzické čoho sa môžeme dotknúť ako napr. auto, lodka, kniha ale aj niečo nehmotné ako návšteva zubára, rezervácia sedadla v kine, bankový účet. Je to čokolvek od čoho chceme spracovať údaje 
Tierdu používame na vytváranie objektov.
    pod menom triedy je meisto pre definovanie našich atribútov t.j. vlastností objektov triedy.

https://www.youtube.com/watch?v=m_MQYyJpIjg 

Abstrakcia znamená zjednodušenie reality. Napr. osoba (Persona) je objekt ale ak by sme navrhovali novú aplikáciu na spracovanie údajov o osobe je nepravdepodobné že by nás zaujímalo všetko čo sa o danej osobe dá vedieť a skôr by sme sa zaoberali údajmi 
ktoré súvisia s úlohou ktorú chceme s týmito údajmi vykonávať 

-------------------------------------------------------------

** Polymorfizmus** je použitie rovnakého názvu funkcie, ale s rôznymi parametrami, pre rôzne dátové typy. Umožňuje objektom volánie metódy s rovnakým menom, ale s inou implementáciou.

Odkazy:\
https://www.javatpoint.com/polymorphism-in-python resp.\
https://www.geeksforgeeks.org/polymorphism-in-python/ \
https://www.w3schools.com/python/python_polymorphism.asp

Príklad zabudovanej (buil-in) funkcie s vlastnosťou polymorfizmu
~~~
# Program Pythonu na demonstrovanie zabudovanej funkcie polymorfizmu 
  
# funkcia len() je pouzita pre string (retazec)  
print (len("Javatpoint"))  
  
# funkcia len() je pouzita pre list (zoznam)  
print (len([110, 210, 130, 321]))  
~~~

Príklad užívateľom definovanej funkcie s polymorfizmom

~~~
# tu je jednoducha funkcia pythonu  
# pre demonstrovanie polymorfizmu  
 
def add(p, q, r = 0):  
    return p + q + r  
  
# Driver code  
print (add(6, 23))  
print (add(22, 31, 544))  
~~~

Príklad funkcie (metódy) použitej v riede

Uvedený príklad demonštruje, ako môže Python používať rôzne typy tried rovnakým spôsobom. Sú tu vytvorené slučky (cykly), ktoré iterujú cez viacero objektov. Ďalej sú volané metódy bez toho, aby ste sa starali o to, do akej triedy každý objekt patrí. Predpokladá sa však, že tieto metódy existujú v každej triede.
~~~
class xyz():  
    def websites(self):  
        print("Javatpoint je webova stranka z mnohych ktore su dostupne na sieti.")  
  
    def topic(self):  
        print("Python sa netyka tem o techologiach Javy.")  
  
    def type(self):  
        print("Java je vyvyjana webova stranka.")  
  
class PQR():  
    def websites(self):  
        print("Pinkvilla je webova stranka z mnohych ktore su dostupne na sieti.")  
  
    def topic(self):
        print("Celebrity su mimo mnohych tem.")  
  
    def type(self):  
        print("pinkvilla je vyvyjana webova stranka.")  


# Vytvorenie objektov a volanie rovnakych metod cez cyklus for

obj_jtp = xyz()     # vytvorenei objektu prvet triedy s menom xyz
obj_pvl = PQR()     # vytvorenei objektu prvet triedy s menom PQR
for domain in (obj_jtp, obj_pvl):  
    domain.websites()  
    domain.topic()  
    domain.type()  
~~~

Vysvetlenie polymorfizmu prostreníctvom **class diagramu** pomocou [videa](/VIII_OOP_s%20_Pythonom/07_Polymorfizmus.mp4)


**Inheritance** čiže dedičnosť je vytvorenie novej triedy ktorá zdedí všetky metódy a vlastnosti z inej triedy. rozlišujeme pri tom *triedu nadradenú* a *triedu podradenú*.

<u>Nadradená trieda</u> je trieda, z ktorej sa dedí, nazývaná aj základná trieda.

<u>Podradená trieda</u> je trieda, ktorá dedí z inej triedy, nazývanej aj odvodená trieda.

Odkazy:\
https://www.javatpoint.com/inheritance-in-python resp.\
https://www.geeksforgeeks.org/inheritance-in-python/ \
https://www.w3schools.com/python/python_inheritance.asp


**Encapsulation**
Popisuje myšlienku zabaľovania údajov a metódy, ktoré pracujú s údajmi v rámci jednej jednotky. To kladie obmedzenia na priamy prístup k premenným a metódam a môže zabrániť náhodnej modifikácii údajov.

Vieme, že trieda je užívateľom definovaný prototyp objektu. Definuje množinu dátových členov a metód, ktoré sú schopné dáta spracovať. Podľa princípu zapuzdrenia dát sú dátové členy, ktoré popisujú objekt, skryté pred prostredím, ktoré je pre triedu externé. Sú dostupné na spracovanie len metódami definovanými v rámci triedy. Na druhej strane samotné metódy sú prístupné z vonkajšieho kontextu triedy. Preto sa o objektových dátach hovorí, že sú zapuzdrené metódami. Výsledkom takéhoto zapuzdrenia je, že sa zabráni akémukoľvek neoprávnenému prístupu k údajom o objekte.

O členovi triedy sa hovorí, že je verejný, ak k nemu možno pristupovať odkiaľkoľvek v programe. Súkromní členovia majú povolený prístup iba z triedy. Zvyčajne sú metódy definované ako verejné a premenné inštancie sú súkromné. Toto usporiadanie premenných súkromných inštancií a verejných metód zabezpečuje implementáciu zapuzdrenia. Na rozdiel od týchto jazykov Python nemá žiadne ustanovenie, ktoré by špecifikovalo typ prístupu, ktorý môže mať člen triedy. V predvolenom nastavení sú všetky premenné a metódy v triede Pythonu verejné, ako ukazuje nasledujúci príklad.

Príklad 1
Tu máme triedu Zamestnanec s premennými inštancie, menom a vekom . Objekt tejto triedy má tieto dva atribúty. Sú prístupné priamo mimo triedy, pretože sú verejné.
~~~
class Student:
   def __init__(self, name="Rajaram", marks=50):
      self.name = name
      self.marks = marks

s1 = Student()
s2 = Student("Bharat", 25)

print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))
~~~
Výsledkom je :
Name: Rajaram marks: 50
Name: Bharat marks: 25

Vo vyššie uvedenom príklade sú premenné inštancie inicializované vo vnútri triedy. Neexistuje však žiadne obmedzenie prístupu k hodnote premennej inštancie mimo triedy, čo je proti princípu zapuzdrenia.

Hoci neexistujú žiadne kľúčové slová na vynútenie viditeľnosti, Python má konvenciu pomenovania premenných inštancie zvláštnym spôsobom. V Pythone predpona názvu premennej/metódy jednoduchým alebo dvojitým podčiarkovníkom na emuláciu správania modifikátorov chráneného a súkromného prístupu.

Ak je pred premennou jednoduché dvojité podčiarknutie (napríklad „ **__age** “), premenná inštancie je súkromná, podobne ak pred názvom premennej je jednoduché podčiarknutie (napríklad „ **_salary** “).

Príklad 2
Upravme triedu Študent. Pridajte ďalšiu inštanciu variabilného platu. Označte meno ako súkromné ​​a označte ho ako súkromné ​​tak, že k nim pridáte dvojité podčiarkovníky.
~~~
class Student:

   def __init__(self, name="Rajaram", marks=50):
      self.__name = name
      self.__marks = marks
   def studentdata(self):
      print ("Name: {} marks: {}".format(self.__name, self.__marks))
      
s1 = Student()
s2 = Student("Bharat", 25)

s1.studentdata()
s2.studentdata()
print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
print ("Name: {} marks: {}".format(s2.__name, __s2.marks))
~~~
Výsledkom je :
Name: Rajaram marks: 50
Name: Bharat marks: 25
Traceback (most recent call last):
 File "C:\Python311\hello.py", line 14, in <module>
  print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
AttributeError: 'Student' object has no attribute '__name'

Vyššie uvedený výstup objasňuje, že názov a vek premenných inštancie, aj keď k nim možno pristupovať pomocou metódy deklarovanej vo vnútri triedy (metóda studentdata()), ale keďže predpona dvojitého podčiarknutia robí premenné súkromnými, a teda k nim pristupujeme mimo trieda je zakázaná, čo spôsobuje chybu atribútu.

Python neblokuje prístup k súkromným údajom úplne. Necháva to na múdrosti programátora, nepíše žiadny kód, ktorý k nemu pristupuje mimo triedy. Stále môžete pristupovať k súkromným členom pomocou Pythonovej techniky mandlovania mien.

Zmena názvu je proces zmeny názvu člena s dvojitým podčiarknutím na tvar **object._class__variable**. Ak je to potrebné, stále je možné k nemu pristupovať aj mimo triedy, ale praktiku by ste sa mali zdržať.

V našom príklade sa premenná súkromnej inštancie "__name" zmení na formát
~~~
obj._class__privatevar
~~~

Ak chcete získať prístup k hodnote premennej inštancie "__marks" objektu "s1", zmeňte ju na "s1._Student__marks".

Zmeňte príkaz print() vo vyššie uvedenom programe na -
~~~
print (s1._Student__marks)
~~~
Teraz vytlačí 50, značky s1.

Preto môžeme konštatovať, že Python neimplementuje zapuzdrenie presne podľa teórie objektovo orientovaného programovania. Prispôsobuje tomu zrelší prístup tým, že predpisuje konvenciu názvov a umožňuje programátorovi používať mangľovanie mien, ak sa skutočne vyžaduje prístup k súkromným údajom vo verejnom rozsahu.


Odkazy:\
https://www.javatpoint.com/encapsulation-in-python \
https://www.tutorialspoint.com/python/python_encapsulation.htm 
https://www.geeksforgeeks.org/encapsulation-in-python/




**class diagram**



Odkazy:\
https://www.javatpoint.com/uml-class-diagram\

https://www.geeksforgeeks.org/unified-modeling-language-uml-class-diagrams/
