class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.introduce_yourself()

    def introduce_yourself(self):
        print(f"Hi I am {self.name} {self.surname}")


michal = Person("Michal", "Hucko")
katka = Person("Katka", "Huckova")
