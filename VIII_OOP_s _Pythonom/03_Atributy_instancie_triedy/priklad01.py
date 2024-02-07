class Person:
    pi = 3.1415

    def __init__(self, name):
        self.name = name


misko = Person("Misko")
katka = Person("Katka")


print(misko.pi)
print(katka.pi)
print(Person.pi)

print(misko.name)
print(katka.name)
