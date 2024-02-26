def compute(arg1, arg2, other):
    print(arg1 + arg2 % other)
    return arg1 + arg2 % other


print(compute(5, 2, 3))

'''class Person(object):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def compute(self, other):
        """ Example of bad class design, don't care about the result """ 
        return self.arg1 + self.arg2 % other

print(Person.compute(5, 2)) 

 Pokúšate sa volať computemetódu v triede Personbez toho, 
 aby ste vytvorili jej inštanciu. Metóda computeje metóda 
 inštancie, takže by sa mala volať na inštanciu triedy. 
 
Treba vytvoriť inštanciu triedy Persona potom zavoláte
 metódu ompute  na tejto inštancii. Vo vašom pôvodnom kóde 
 ste sa pokúšali volať metódu compute  priamo v triede, 
 čo nie je správny spôsob použitia metód inštancie. 
 Týmto spôsobom vytvoríte inštanciu triedy Person a 
 potom zavoláte metódu compute na tejto inštancii. 
 
'''

class Person(object):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def compute(self, other):
        """Example of bad class design, don't care about the result"""
        return self.arg1 + self.arg2 % other


# Create an instance of Person
person_instance = Person(5, 2)

# Call the compute method on the instance
result = person_instance.compute(5)
print(result)
