V pythone inštancia odkazuje na objekt vytvorený z triedy. Keď vytvoríte inštanciu triedy,  vytvoríte inštanciu tejto triedy. **Inštancie** sú jedinečné objekty s atribútami a správaním definovaným triedou do ktorej patria. Inštancie vám umoŹňujú pracovať a manipulovať s konkrétnými objektami vo vašom programe v pythone.

V pythone inštancia odkazuje na konkrétny výskyt alebo realizáciu triedy a vytvára objekt založený na tejto triede. Inštancie sú jednotlivé objekty vytvorené z plánu triedy a majú svoje vlastné jedinečné atribúty a správanie definované triedou.


V pythone je **premenná inštancie** premenná ktorá patrí ku konkrétnej **inštancii tiredy**. Každý objekt vytcorený z triedy môže mať svoju vlastnú množinu inštancii premenných, ktoré sú definované v rámci metód triedy. Tieto premenné  ukladajú údaje jedinečné pre každú inštanciu a pristupuje sa k nim pomocou bodkovej konvencie.

V pythone je inštancia triedy objekt vytcorený z triedy. Predstavuje špecifický výskyt tejto triedy, ktorý má vlastný súbor atribútov a správania definovaných triedou. Inštancie vám umožňujú pracovať s vlastnosťami a metódami ktoré sú špecifikované v pláne tirdy n azáklade jednotlivých objektov.


V pythone je metóda inštancie funkcia definovaná v rámci triedy a je spojená s inštanciou tejto triedy. Za svoj prvý parameter berie samostatnú inštanciu s konvenčným názvom **self** čo jej umožňuje pristupovať k atribútom inštancie a manipulovať s nimi. Metódy inštancie sa volajú na inštanciách triedy a môžu pracovať so špecifickými údajmi tejto inštancie.

Čo umožňuje OOP je tvoriť vlastné objekty s vlastnými metódami (tzv. encapsulation čo znamená že pevne zviažeš nejaké operácie iba ku konkrétným objektom) a týto metódy medzi nimi odovzdávať (dedičnosť a pod.) Inými slovami ak by sme s vytvorenou triedou Person (v respektíve s ich inštanciami) vykonával vicer operácii ako iba vypísanie mena/priezviska, je to značná úšpora, ktorá môže tiež prispieť k čitatelnosti kódu. 
Myslieť objektívne nie je ľahká úloha, ale ak človek prejde cez začiatky , otvoria sa mu nové dvere a možnosti ako nad kódom ako takým premýšlať.

V Pythone je metóda __init__   metódou inštancie. Je to ale špeciálna metóda, ktorá sa volá, keď je objekt vytvorený z triedy. Používa sa na inicializáciu atribútov objektu. Parameter self v metóde __init__  odkazuje na inštanciu triedy a používa sa na prístup a úpravu atribútov objektu.

Tu je jednoduchý príklad:
~~~
class MyClass:
    def _init_(self, x, y):
        self.x = x
        self.y = y

# Vytvorenie instancie/objektu triedy MyClass
obj = MyClass(1, 2)

# Accessing attributes of the instance
print(obj.x)  # Vystup: 1
print(obj.y)  # Vystup: 2
~~~

V tomto príklade __init__ je to metóda inštancie a self sa používa  na odkazovanie na inštanciu ( obj ), ktorá sa vytvára.

V Pythone je atribútom premenná inštancie, ktorá patrí ku konkrétnej inštancii triedy. Každý objekt vytvorený z triedy môže mať pre atribúty inštancie svoje vlastné jedinečné hodnoty. Tieto atribúty sú síce definované iba v rámci triedy, ale sú špecifické pre každú inštanciu tejto triedy.

~~~
class Dog:
    def _init_(self, name, age):
        self.name = name  # 'name' je atribut instancie
        self.age = age    # 'age' je ďalším atribútom inštancie

# Vytvotrenie dvoch instancii triedy Dog
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Prístup k atribútom inštancie
print(dog1.name)  # Vystup: Buddy
print(dog2.age)   # Vystup: 5
~~~

V tomto príklade name a age sú atribúty inštancie špecifické pre každý objekt dog ktore sú vytvorené z triedy Dog .