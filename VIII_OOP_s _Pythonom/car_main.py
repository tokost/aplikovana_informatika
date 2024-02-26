# car.py
class Car:
    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")


# main.py
from car import Car

make = "Chevy" 
model = "Corvette"
year = 2021
color = "modra"

car_1 = Car()
car_1.drive()
car_1.stop()
