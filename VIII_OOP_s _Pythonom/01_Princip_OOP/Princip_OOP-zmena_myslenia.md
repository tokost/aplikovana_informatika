>## Princíp OOP – Objektovo Orientovaného Programovania

 Objektovo Orientované Programovanie (OOP) sa vykonáva pomocou Objektovo Orientovaného Programovacieho Jazyka (OOPJ) ako je napr. Python, Java, C++ a pod. Toto programovanie úzko súvisí s pojmami ako **trieda, objekt, metóda, inštancia** atď. a  predovšetkým vyžaduje objektovo myslieť. Je to niečo úplne iné od prístupu ktorý sa používal v [starších imperatívnych PJ](https://www.computerhope.com/jargon/i/imp-programming.htm). kde program popisuje kroky, ktoré menia stav počítača. Na rozdiel od deklaratívneho programovania, ktoré popisuje „čo“ by mal program dosiahnuť, **imperatívne programovanie explicitne hovorí počítaču „ako“ to dosiahnuť**. Patrí k nim napr. C/C++, Pascal, Basic, Assembler a pod. 
 
 ![](/VIII_OOP_s%20_Pythonom/obrazky/prog_jaz01.png)
 
 Objektovo orientované programovacie jazyky síce tiež vychádzajú zo skupiny imperatívnych jazykov avšak na rozdiel od kategórie procedurálných PJ ktoré do postupnosti krokov ktoré má počítač vykonávať zavádzajú určitú organizáciu v podobe vytvárania skupín - procedúr, sú OOPJ založené na koncepcii vytvárania objektov. Rozdiely medzi týmimito dvomi druhmi programovacích jazykov najlepšie zobrazuje priložená tabuľka:

 ![](/VIII_OOP_s%20_Pythonom/obrazky/prog_jaz02.png)

 Preto je veľmi dôležité aby sme sa skôr než pristúpime k poznávaniu daného OOPJ najprv zonámili s tým čo to znamená objektovo myslieť a definovať objekty. 
 
 Pri ostatných PJ sme program vytvárali tak, že sme chronologicky  pod seba zostavovali jednotlivé programové príkazy, ktoré napr. interpreter (program ktorý ich okamžite spracováva) aresp. kompilátor (program ktorý ich spracuje všetky naraz) vykonáva postupne jeden po druhom smerom z hora nadol.

OOP však predstavuje úplne odlišný prístup k vytváraniu a vykonávaniu programu a komunikácii medzi jeho jednotlivými časťami. Na tomto prístupe je založené každé OOP a to či už vytvárame nejaké malé programy napr. utility alebo veľké a zložité programy napr. z oblasti webových aplikácii s databázovou podporou.

Odlišnému spôsobu [myslenia](https://www.itnetwork.sk/java/oop/java-tutorial-uvod-do-objektovo-orientovaneho-programovani)  a teda odlišnému prístupu k riešeniu úloh a problémov potom zodpovedá aj odlišný spôsob vytvárania programu a jeho odlišná štruktúra. Tá je spravidla pre každý OOPJ daná jeho vlastnou syntaxou, na základe ktorej sa jednotlivé OOPJ navzájom odlišujú. Na základe týchto skutočností bez nadsádzky možno konštatovať že OOPJ priniesli do oblasti vývoja softvéru novú éru. Je to prirodzený dôsledok [evolúcie](https://www.petrzalka.sk/wp-content/uploads/2012/12/3_Evolucia_ZS_Gessayova_7A.pptx ), napredovania a zákonitého vývoja v oblasti výpočtovej techniky a programovania .

![](/VIII_OOP_s%20_Pythonom/obrazky/evolucia.png)

V čom teda spočíva to nové myslenie a čvo je ďspecifické pre OOPJ ? Pri OOP sa najprv **snažíme vytvoriť abstrakciu reálneho objektu v podobe jeho modelu**, vzoru či šablóny. 

Robíme to preto lebo chceme **získať obraz ktorý zodpovedá realite** a mohli na tomto obraze simulovať jeho správanie. Chceme na tomto **modely nastaviť podmienky ktoré zodpovedajú realite** bežného života a zaujímajú nás reakcie ktoré vyhodnocujeme a ev. na základe ktorých meníme podmienky. To nám nakoniec pomocou takéhoto modelovania napovie čo a ako musíme nastaviť v reálnom živote aby sme dostali očakávané výsledky. 

Takýmto spôsobom sa na rozdiel od spracovávaní procedurálneho typu programu **odpútavame od prispôsobovaniu sa stroju** a princípov na základe ktorých pracuje počítač. A pri písaní objektovo orientovaného typu programu **zohľadňujeme iba pohľad programátora - človeka**.  

Myšlienka je taká, že namiesto toho, aby sme všetko písali ako nudnú sekvenciu programovacích inštrukcií, môžeme veci modelovať a definovať ako sa navzájom ovplyvňujú.

Ak chceme modelovať mačku, vytvoríme objekt Cat, ktorý má nejaké vlastnosti ako color, age, mood (nálada: dobrá, zlá alebo ospalá) a owner (ktorý by mohol byť priradený objektu Person – resp. v prípade zatúlania mačky, by táto vlastnosť bola prázdna).

Potom nad objektom Cat možno registrovať niekoľko aktivít - akcií: purr (pradie), scratch (škrábe), alebo feed (žerie) (v takom prípade dáme mačke nejaké CatFood (mačacie žrádlo), čo môže byť samostatný objekt s vlastnosťami, napríklad taste (chuť)).

~~~
Cat
--------
color
age
mood
owner
purr()
scratch()
feed(cat_food)
~~~
~~~
CatFood
--------
taste
~~~

Takže v podstate ide o opísanie skutočných vecí v pragramovom kóde s vlastnosťami (nazývanými **object properties**) a akciami (nazývanými **methods**).


Ako potom budeme modelovať blogové príspevky? Chceme si totiž vytvoriť vytvoriť aplikáciu na písanie a komentovanie blogu.

Preto si musíme odpovedať na otázku: Čo je to blogový príspevok? Aké vlastnosti by mal mať?

Náš blogový príspevok určite bude obsahovať nejaký text s obsahom a názvom. Bolo by tiež dobré vedieť, kto to napísal – takže potrebujeme autora. Nakoniec chceme vedieť aj to, kedy bol príspevok vytvorený a publikovaný t.j. vložený na web. Jeho vlastnosti potom možno zhrnúť takto:


~~~
Post
--------
title
text
author
created_date
published_date
~~~

Ešte však potrebujeme vedieť aké veci resp. činnosti (metódy) by sa mali robiť s blogovým príspevkom. Bolo by dobré mať niekoho method (funkcii), ako napr. kto uverejní príspevok a pod.
Za týmto účelom budeme teda potrebovať metódu ktorú nazveme **publish**. Keďže už vieme, čo chceme dosiahnuť, môžeme začať modelovať.


Pre vývoj programovacích jazykov je príznačný prechod od strojovo orientovaných jazykov cez  assembler k jazykom s čitateľnejším zápisom zápisom kódu, ktoré budú tiež s veľkou pravdepodobnosťou v budúcnosti nahradené novšími technológiami. Pri OOP však ide pri riešení danej úlohy o prelomovú technológiu, ktorá prináša do programovania určitú úroveň abstrakcie ( vytvárania modelu budúcej reality). Takýto prístup má značné výhody v tom, že na jednej strane postupne získavame predstavu o budúcom výsledku a na strane druhej pri zmene parametrov zadania nenastanú žiadne výraznejšie komplikácie s prerábaním kódu. 

![](/VIII_OOP_s%20_Pythonom/obrazky/oop.png)


### Aplikácia OOP v programovacom jazyku Python.
(vysvetlenie pojmov podľa Miša)

Projekt domu v sebe zahŕňa jednotlivé časti domu. Dom je v ňom nakreslený v rôznych pohľadoch a projekt tiež obsahuje ďalšie informácie ako sú veľkosti a výšky stien, počte poschodí a pod.

![](/VIII_OOP_s%20_Pythonom/obrazky/rodinny_dom.png)
![](/VIII_OOP_s%20_Pythonom/obrazky/projekt01.png) ![](/VIII_OOP_s%20_Pythonom/obrazky/projekt02.png)

Projekt je však nakreslený iba na papieri a my vieme podľa tohto projektu postaviť mnoho rovnakých skutočných – reálnych domov. Ak ale chceme aby sa náš dom odlišoval od pôvodného návrhu, stačí nám jednoducho zmeniť niektoré vlastnosti - atribúty uvedené v projekte ako sú napr. rozmery pozemku, počet izieb a pod. 

Dôležité je to, že v samotnom projekte nemôžeme bývať (je to iba abstrakcia - model budúcej reality skutočného obývateľného domu, ktorý je nakreslený na papieri). Je to teda iba papier ktorý nesie informácie o tom ako bude budúci realny dom. 

A PRESNE TAK JE TO AJ V OBJEKTOVO ORIENTOVANOM PROGRAMOVANÍ. Ten projekt je naša trieda (Trieda ako definícia konkrétnych objektov – blueprint t.j. návod alebo **plán podľa ktorého budeme postupovať**) a teda **pomocou tohto projektu alebo pomocou tejto triedy vieme vytvárať konkrétne objekty** – domy. Na to aby sme však vytvorili objekt potrebujem jeho triedu tak isto ako potrebujem pre vytvorenie domu jeho projekt. Čiže tento projekt nám pomáha vytvárať naše domy. 




Čiže posielam zatiaľ iba akýsi prázdny objekt. Do konštruktora ďalej posielame premenné ktoré budú definovať stav objektu. Takže si predstavme podľa obrázku že chceme vytvárať nejaké osoby pomocou triedy (class) osoba (Person). Každá osoba bude pozostávať z mena(name_p) a priezviska (surname_p) taže do konštruktora budeme zdola t.j. z tela triedy posielat name_p a surname_p. Nasledne v tele konštruktora definujeme že každý objekt self bude mať name_p (self.name_p) ktorý sa rovná premennej ktorá prišla do konštruktoru (name_p). Podobne definujem že každý objekt self.surname_p bude mať v sebe priezvisko surname_p ktoré prišlo z konštruktora. TAKÝMTO SPOSOBOM DEFINUJEME STAV OBJEKTU v časti konštruktora.
SPRAVANIE OBJEKTU sa definuje mimo konštruktor pomocou metód alebo funkcii. Tie vytvárame opäť pomocou kľúčového slovíčka def .Podobne ako predchádzajúca funkcia aj táto funkcia pozostáva z názvu a definície parametrov. Na názov opäť používame Snake Case všetko s malým písmom. V časti správania
je opäť prvým parametrom self lebo keď chceme v tele správania využiť jednotlivé premenné alebo iné funkcie tohto objektu, tak k nim pristupujeme cez self. Napríklad v tejto časti funkcia alebo metóda vypisuje meno osoby a preto v časti print pristupuje k menu daného objekt , ale už reálneho objektu mimo triedy, pomocou self. Pomocou príkladov bude možné tieto skutočnosti názorne demonštrovať a pochopiť (Lekcia 2).
Vo vyššie uvedenom sme vytvárali definíciu triedy. Vyvstáva však ešte otázka ako vytvoríme objekt ? Veľmi jednoducho ! V ďalšom riadku nášho kódu mimo odsadenia triedy teraz vieme vytvárať inštanciu alebo objekt. Pojem inštancie je iba synonymom slovíčka objekt. Teda keď hovoríme inštancia myslíme tým objekt. A vytvoríme ich tak že zavoláme názov triedy (s veľkým písmenom na začiatku ) a tak ako tomu bolo v prípade funkcie zavoláme nad ním okrúhle zátvorky.. A v tomto prípade priamo voláme konštruktor tejto triedy. A konštruktor v našom prípade našej osoby pozostával z mena priezviska. Bol tam síce pred tým ešte ten self, avšak keď voláme konštruktor môžeme tento self ignorovať a posielam parametre mimo self. Čiže pošleme iba konkrétne – reálne meno a priezvisko. Inštancia resp. objekt pre Person potom bude vyzerať nasledovne Person(“Michal“, “Hucko“).
Takýmto spôsobom sa vytvorí objekt. Tento objekt si môžeme priradiť do premennej, do poľa, do akejkoľvek konštrukcie či už jednoduchej alebo zložitej. Následne vieme pristupovať k jeho atribútom alebo stavu toho daného objektu
cez tzv. bodkovú konvenciu. Môžem meniť stav objektu cez bodku a taktiež môžem volať cez bodku jeho správanie. Pozor self existuje iba pri definícii t.j. pri vytváraní triedy !!!


