https://pythontutor.com/python-compiler.html

# Priklad definicie triedy. Prakticky ale zbytocnej triedy 
# lebo nepouziva atributy a uloha by sa dala naprogramovat
# jednoduchsie bez pouzitia triedy. Ide vsak o nazornost

class Person:
    name = "Michal"
    def print_name():
        print(f"Meno je {Person.name}")

Person.print_name()

# Trieda je nejaky predpis, sablona, vzor niecoho. A v tomto pripade
# je to predpis ktory sa tyka osoby a ktory hovori ze osoba ma meno a priezvisko

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

# Potrebujeme spracovavat prispevky. Navrhnite triedu a atributy. Ako metodu
# pouzijeme iba zobrazenie udajov na monitore