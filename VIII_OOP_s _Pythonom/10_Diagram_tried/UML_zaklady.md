https://sbcode.net/python/uml_diagrams/

Diagramy Unified Modeling Language (UML) sa v tejto knihe používajú ako pomôcka pri popise vzorov.
Nižšie je niekoľko príkladov, ktoré popisujú UML diagramy.

Ľavá časť diagramu zobrazuje základný koncept a pravá strana ukazuje potenciálny príklad použitia.

**Entita triedy**

![](/basic_uml01.png)

* public - znamená že triedy alebo objekty, ktoré majú prístup z vonka tiedy k tomuto atribútu alebo metóde, môžu čítať a zapisovať ich hodnotu a môžu vyvolať ich správanie. odkiaľkoľvek v systéme. Dá sa k nemu dostať odkiaľkolvek a má predponu symbol „+“.
* private - znamená že k prvku (atribútu resp. metóde) nie je prístup zvonka triedy a je viditelný a použitelný iba v rámci triedy ktorá ho vlastní. Nedá sa k nemu dostať mimo triedy. Súkromný prvok má predponu symbol '−'
* **#** - protected znamená chránená viditeľnosť t.j. je viditeľný zvnútra triedy a z podtried zdedených z tejto triedy, ale nie zvonku.
* void - je parameter funkcie ktorá nič nevracia resp. v pythone sa vracia tzv. **None** čo špeciálny objekt Pythonu pre „nič“

Pri class diagramov rozlišujeme predovšetkým tieto vzťahy:

![](/typy_vztahov01.png)

kde\
**Dependency**  - vyjadruje závislosť
**Association** - vyjadruje združenie
**Direct Assotiation** - vyjadruje jurčené združenie
**Inheritance** - 
**Realisation** - 


**Dependency (Závislosť)** \



**Association (Združenie)** \
Používa sa na vyjadrenie vzťahu v rámci jednej triedy. Vvyjadruje väzby medzi objektmi tejto triedy. Inými slovami, možno povedať, že asociácia označovaná aj ako reflexná, pozostáva na druhej strane z prvkov ktoré predstavujú objekty t.j. inštancie rovnakej triedy. Ako príklad uvedieme triedu zeleniny ktorá má dva objekty, napr. cibuľu a baklažán. Podľa definície asociácie existuje spojenie medzi cibuľou a baklažánom, keďže patria do rovnakej triedy. Tým spojením je trieda zelenina.

![](/basic_uml05.png)

**Directed Association (Určené združenie)**\
Používa sa na vyjadrenie vzťahu medzi dvomi a viacerými triedami. Čiara je ukončená šípkou resp. vyplnenou šípkou  určuje ktorá tieda používa ktorú inú triedu. Vyjadrené je to práve smerovaním tejto šípky. V príklade **ClassA** používa **ClassB** alebo objekt **ClassB** a preto šípka smeruje od ClassA smerom ku ClassB.

![](/basic_uml02.png)

ClassA volá metódu statickej triedy, statickú abstraktnú metódu alebo metódu/vlastnosť/pole z objektu typu ClassB. Napr. **Person** naštartuje **Car**

**Inheritance (Zdedenie)**\
Čiara ktorá je ukončená nevyplnenou šípkou ukazuje na triedu, ktorá je zdedená a rozširuje triedu od ktorej táto šípka vychádza.

![](/basic_uml03.png)

Nech trieda A (Class) rozširuje triedu B (ExtendedClass), tak že ExtendedClass zdedí Class. Rozšírená trieda potom obsahuje všetky atribúty/polia a metódy zdedenej triedy, vrátane jej vlastných extra metód, atribútov/polí, prepisov a preťažení.


**Realisationm (Realizácia)**\ 

 
**Aggregation (Agregácia-Zhromaďenie)**\
Keď hovoríme že ClassA agreguje ClassB tak to znamená že napr. knižnica ktorú reprezentuje ClassA zhromažďuje knihy ktoré reprezentuje ClassB. Vyjadrené je to čiarou ktorá na svojom začiatku obsahuje prázdny kosoštvorec a na agregovanú triedu môže ukazovať šípka. Knihy a knižnica však môžu existovať nezávisle od seba. Knihy môžu existovať aj bez knižnice.

![](/basic_uml06.png)

Pokiaľ je kosodlžník vyplnený označuje to **Kompozíciu (Composition)** t.j. že jedna trieda napr ClassA sa skladá z inej triedy napr. ClassB. Ako príklad môžeme uviesť lietadlo ktoré sa musí skladať z krídel a iných častí. Ale bez krídiel už lietadlo neplní funkciu lietadla a teda v skutočnosti už nie je vlastne lietadlom ale iba šrotom.

![](/basic_uml07.png)

Niekedy sa pri class diagramoch stratneme so vzťahom ktorý vyjadruje anotáciu tzv. pseudokódu.

![](/basic_uml08.png)

Je to rámček označený s prerušovanou čiarou a kruhom umiestneným blízko metódy triedy. Pseudokód je jednoduchý jazykový popis krokov v algoritme a používa sa na zobrazenie konceptu bez potreby písať dlhé riadky kódu.
