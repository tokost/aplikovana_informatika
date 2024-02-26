# car.py
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")


# main.py
from car import Car

make = "Toyota"  # Example values
model = "Camry"
year = 2022
color = "Blue"

# Create an instance of the Car class
my_car = Car(make, model, year, color)

# Call methods on the instance
my_car.drive()
my_car.stop()
