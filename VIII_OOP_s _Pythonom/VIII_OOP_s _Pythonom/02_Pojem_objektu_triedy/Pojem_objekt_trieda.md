Základným pojmom OOP je **objekt** ktorý zodpovedá nejakému objektu z reálneho sveta (napr. dom, človek, učiteľ, auto, mačka, databáza alebo príspevok). **Objekt má svoje vlastnosti (atribúty) a vie vykonávať nejaké činnosti (metódy resp. funkcie)**. Atribúty sú údaje, ktoré sú všeobecne pre objekt charakteristické (napr. u človeka je to meno a vek, u databázy heslo atď.). Pri programovaní na vyjadrenie atribútov môže použiť datový typ premennej a v prípade človeka to môže byť napr. name a age. S týmito vlastnosťami človeka sme sa v bežnom živote už veľa krát stretli a pri programovaní sme už tiež asi takéto premenné použili. O týchto premenných, ktoré reperezentujú vlastnosti objektu hovoríme aj ako o vnútornom stave objektu nakoľko ho charakterizujú.

![](/obrazky/rodinny_dom.png)
![](/obrazky/projekt01.png) ![](/obrazky/projekt02.png)

![](/obrazky/person.png) ![](/obrazky/ucitel.png) ![](/obrazky/databaza.png) ![](/obrazky/automobil.png)

**Metódy vyjadrujú činnosti alebo funkcie, ktoré vedia objekty vykonávať alebo ktoré je možné nad objektami vykonávať**. U človeka by to mohli byť napr metódy: chodDoPrace(), pozdrav() alebo mrkni_okom() a pod. U databázy zase pridajZaznam() alebo vyhľadaj_Zaznam(), pri objekte Príspevok zase vytvor_Príspevok(), zmaz_Prispevok() a pod. Metódy môžu mať parametre a môžu tiež vracať nejakú hodnotu. 

Ďalším základným pojmom je **trieda**(angl. class). **Trieda je vzor, predpis alebo šablóna, podľa ktorej sa vytvárajú objekty**. Preto triedu tak ako objekty definujú tiež vlastnosti (atributy) a činosti (metódy) ktoré je možné s alebo nad atribútami vykonávať. Uskutočňuje sa to príkazom ktorý nasleduje bezprostredne po definícii triedy a ktorý sa nazýva **konštruktor**. Jeho syntax je nasledovná:

~~~
def __init__(self, prvy_atribut, druhy_atribut, ...): 
~~~

Objekt, ktorý sa vytvorí podľa vzoru triedy, sa nazýva **inštancia triedy** .Je to niečo ako premenná triedy a na rozdiel od triedy má alokovanú t.j. vyčlenenú pamäť. Niekedy inštanciu triedy voláme aj objekt lebo **inštancia je špecifická realizácia akéhokoľvek objektu**. Objekt vytvorený na danej triede môže byť odlišný v rôznych smeroch a každý vytvorený variant objektu je inštanciou danej triedy. 

Pre nás preto budú tieto dva termíny úplné rovnocenné a keď budeme hovoriť o objekte myslíme tým aj inštanciu triedy a naopak. **Inštancie** majú rovnaké rozhranie ako trieda (v podobe atribútov), podľa ktorej sa vytvárajú, ale **navzájom sa líšia svojimi dátami (t.j. hodnotami atribútov)**. Rozhranie je miesto medzi triedou a nad ňou vytvoreným objektom kde dochádza k vzájomnej výmene údajov prostredníctvom atribútov. 

Zatiaľ čo **trieda je** pri tomto vzťahu  prostredníctvom svojho konštruktora iba **predpisom o počte a názve svojich atribútov** prostredníctvom ktorých dochádza k výmene údajov, **objekt je** iba **nositeľom konkrétnych reálnych údajov** pre jednotlivé definované atribúty. 

Zoberme si ako príklad **triedu Person (Osoba)** na ktorej si zadefinujeme dva **atribúty meno a vek** ktoré predstavujú vzor. Ďalej si vytvoríme **inštancie t.j objekty karol a jozef**. Obe inštancie majú tie isté rovnomenné atribúty, ako trieda podľa ktorej boli objekty vytvorené. Je to spomínané meno a vek. Ako **metódy si tu zadefinujeme chodDoPrace() a pozdrav()**. Objekty karol a jozef ktoré sú reálnymi objektami sa však od seba líšia svojimi hodnotami atribútov, kedy *prvá inštancia má v atribúte **meno** hodnotu "karol"* a *v atribúte **vek** hodnotu 22*, druhá "jozef" a 45. To ako tieto skutočnosti vyjadríme v podobe programového zápisu si ukážeme neskôr. 

**Komunikácia medzi objektmi prebieha pomocou vzájomného odovzdávania správ**, vďaka čomu je syntax t.j. spôsob ako sa tieto skutočnosti zapisujú v programe pomocou príkazov jazyka Python  veľmi prehľadná. Vlastná správa totiž všeobecne vyzerá nasledovne: 
~~~
príjemca_spravy.nazov_metody(parametre)
~~~

 Napr. pre náš prípad by tento zápis komunikácie medzi objektami vyzeral nasledovne:
 
~~~
 karol.pozdrav(suseda)
~~~

To by spôsobilo, že inštancia karol pozdraví inštanciu suseda ak by bol parametrom sused tiež objekt. Tomuto zápisu hovoríme bodková notácia a pri písaní programov sa s ňou veľmi často stretávame. 

![](oop.png)
Základným pojmom OOP je **objekt** ktorý zodpovedá nejakému objektu z reálneho sveta (napr. dom, človek, učiteľ, auto, mačka, databáza alebo príspevok). **Objekt má svoje vlastnosti (atribúty) a vie vykonávať nejaké činnosti (metódy resp. funkcie)**. Atribúty sú údaje, ktoré sú všeobecne pre objekt charakteristické (napr. u človeka je to meno a vek, u databázy heslo atď.). Pri programovaní na vyjadrenie atribútov môže použiť datový typ premennej a v prípade človeka to môže byť napr. name a age. S týmito vlastnosťami človeka sme sa v bežnom živote už veľa krát stretli a pri programovaní sme už tiež asi takéto premenné použili. O týchto premenných, ktoré reperezentujú vlastnosti objektu hovoríme aj ako o vnútornom stave objektu nakoľko ho charakterizujú.

![](/obrazky/rodinny_dom.png)
![](/obrazky/projekt01.png) ![](/obrazky/projekt02.png)

![](/obrazky/person.png) ![](/obrazky/ucitel.png) ![](/obrazky/databaza.png) ![](/obrazky/automobil.png)

**Metódy vyjadrujú činnosti alebo funkcie, ktoré vedia objekty vykonávať alebo ktoré je možné nad objektami vykonávať**. U človeka by to mohli byť napr metódy: chodDoPrace(), pozdrav() alebo mrkni_okom() a pod. U databázy zase pridajZaznam() alebo vyhľadaj_Zaznam(), pri objekte Príspevok zase vytvor_Príspevok(), zmaz_Prispevok() a pod. Metódy môžu mať parametre a môžu tiež vracať nejakú hodnotu. 

Ďalším základným pojmom je **trieda**(angl. class). **Trieda je vzor alebo šablóna, podľa ktorej sa vytvárajú objekty**. Preto triedu tak ako objekty definujú tiež vlastnosti (atributy) a činosti (metódy) ktoré je možné vykonávať. Uskutočňuje sa to príkazom ktorý nasleduje bezprostredne po definícii triedy a ktorý sa nazýva **konštruktor**. Jeho syntax je nasledovná:

~~~
def __init__(self, prvy_atribut, druhy_atribut, ...): 
~~~

Objekt, ktorý sa vytvorí podľa vzoru triedy, sa nazýva **inštancia triedy** .Je to niečo ako premenná triedy a na rozdiel od triedy má alokovanú t.j. vyčlenenú pamäť. Niekedy inštanciu triedy voláme aj objekt lebo **inštancia je špecifická realizácia akéhokoľvek objektu**. Objekt vytvorený na danej triede môže byť odlišný v rôznych smeroch a každý vytvorený variant objektu je inštanciou danej triedy. 

Pre nás preto budú tieto dva termíny úplné rovnocenné a keď budeme hovoriť o objekte myslíme tým aj inštanciu triedy a naopak. **Inštancie** majú rovnaké rozhranie ako trieda, podľa ktorej sa vytvárajú, ale **navzájom sa líšia svojimi dátami (t.j. hodnotami atribútov)**. Rozhranie je miesto medzi triedou a nad ňou vytvoreným objektom kde dochádza k vzájomnej výmene údajov prostredníctvom atribútov. 

Zatiaľ čo **trieda je** pri tomto vzťahu  prostredníctvom svojho konštruktora iba **predpisom o počte a názve svojich atribútov** prostredníctvom ktorých dochádza k výmene údajov, **objekt je** iba **nositeľom konkrétnych reálnych údajov** pre jednotlivé definované atribúty. 

Zoberme si ako príklad **triedu Person (Osoba)** na ktorej si zadefinujeme dva **atribúty meno a vek** ktoré predstavujú vzor. Ďalej si vytvoríme **inštancie t.j objekty karol a jozef**. Obe inštancie majú tie isté rovnomenné atribúty, ako trieda podľa ktorej boli objekty vytvorené. Je to spomínané meno a vek. Ako **metódy si tu zadefinujeme chodDoPrace() a pozdrav()**. Objekty karol a jozef ktoré sú reálnymi objektami sa však od seba líšia svojimi hodnotami atribútov, kedy *prvá inštancia má v atribúte **meno** hodnotu "karol"* a *v atribúte **vek** hodnotu 22*, druhá "jozef" a 45. To ako tieto skutočnosti vyjadríme v podobe programového zápisu si ukážeme neskôr. 

**Komunikácia medzi objektmi prebieha pomocou vzájomného odovzdávania správ**, vďaka čomu je syntax t.j. spôsob ako sa tieto skutočnosti zapisujú v programe pomocou príkazov jazyka Python  veľmi prehľadná. Vlastná správa totiž všeobecne vyzerá nasledovne: 
~~~
príjemca_spravy.nazov_metody(parametre)
~~~

 Napr. pre náš prípad by tento zápis komunikácie medzi objektami vyzeral nasledovne:
 
~~~
 karol.pozdrav(suseda)
~~~

To by spôsobilo, že inštancia karol pozdraví inštanciu suseda ak by bol parametrom sused tiež objekt. Tomuto zápisu hovoríme bodková notácia a pri písaní programov sa s ňou veľmi často stretávame. 













OOP stojí na troch základných pilieroch:

* **Zapuzdrenie** -[Encapsulation](https://www.geeksforgeeks.org/encapsulation-in-python/)
* **Dedičnosť** - [Inheritance](https://www.geeksforgeeks.org/inheritance-in-python/)
* **Polymorfizmus** - [Polymorphism](https://www.geeksforgeeks.org/polymorphism-in-python/)
