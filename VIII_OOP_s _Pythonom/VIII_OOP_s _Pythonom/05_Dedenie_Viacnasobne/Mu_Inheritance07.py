# Mu_Inheritance07.py

# Python program to demonstrate super()
                     
class Class1:
    def m(self):
        print("In Class1")
                     
class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()
                     
class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()
                     
class Class4(Class2, Class3):
   def m(self):
        print("In Class4")
        super().m()
                     
print()
print(Class4.mro())		 #This will print list
print()                    
print(Class4.__mro__)	 #This will print tuple
print()