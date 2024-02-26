class Student:
    # premenna triedy
    school_name = 'ABC School'

    # konstruktor
    def __init__(self, name, age):
        # premenne instancie
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
# pristup k premennej instancie
print('Student:', s1.name, s1.age)

# pristup k premennej triedy
print('School name:', Student.school_name)

# modifikacia premennej instancie
s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)

# modifikacia premennej triedy
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)