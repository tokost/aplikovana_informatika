from car import Car

make = "Chevy"  # 2.
model = "Corvette"
year = 2021
color = "modra"

# car_1 = Car("Chevy", "Corvette", 2021, "modra")
car_1 = Car(make, model, year, color)
print(car_1.make) 
print(car_1.model) 
print(car_1.year) 
print(car_1.color)

car_1.drive()
car_1.stop()
