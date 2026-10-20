from car import Car

car1= Car("Mustang", "2024", "red", False)
car2 = Car("Porshe", "1989", "yellow", True)

print(car1.model)
print(car1.year)
print(car1.color)

car2.drive()