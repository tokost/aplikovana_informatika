Príkaz ako zistiť verziu Djanga
**$ pip show django --version**

Príkaz ako zmeniť starý názov hlavnej vetvy master ktorá vzniká po inicializácii git int na názov main ktorý je
súčasne používaný
**$ git branch -m master main**

Inicializácia lokálného repository
**$ git init**

>### Fungujúca komunikácia s GitHub-om

>Zistenie čo nie je uložené v lokálnom repositori
**$ git tatus**

>Ak nie sú nejaké súbory resp. adresáre uložené v lokálnom
repository, tak ich tam pridáme príkazom
**$ git add .**

>Táto transakcia sa uskutoč ní s príkazom commit pri ktorom
mô%zeme zadať aj komenár čo sme na lokálne úlužisko uložili
**$ git commit -m "text o tom čo alebo prečo sme niečo žili na lokálne repository"**

> Nasleduje uloženie zmien a doplnkov na github
**$ git push origin main** resp.
**$ git push -f origin main**

Miesto názvu origin je možné požiť tzv. alias. Definujeme ho  takto:
**$ git remote add "názov_aliasu" "naše URL z githubu príslušného repository"** napr. pre alias ai-gh bude príkaz $ git remote add ai-gh https://github.com/tokost/aplikovana_informatika.git

Prtíkaz push potom bude vždy vyzerať takto:
**$ git push ai-gh main**

>### Nová komunik=acia s GitHub

Ak chceme riešiť sťahovanie z GitHUbu na lokalne repository, tak musíme najprv vytvoriť konektivitu

**$ git pull --allow-unrelated-histories"naše URL z githubu príslušného repository"**

Ak konektivita funguje, tak sťahovanie pomocou aliasu sa robí cez príkaz:$ git pull alias main napr. **$ git pull ai-gh main**