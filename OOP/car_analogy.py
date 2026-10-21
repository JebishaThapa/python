class Car:
    def __init__(self, brand, model, year):
        self.brand = brand   
        self.model = model   
        self.year = year     
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"The engine of the {self.year} {self.brand} {self.model} is now running!")

    def stop_engine(self):
        self.is_running = False
        print(f"The engine of the {self.brand} {self.model} has stopped.")


car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model 3", 2024)

print(f"Car 1 is a {car1.brand} {car1.model}.") 
car1.start_engine()

print(f"\nCar 2 is a {car2.brand} {car2.model}.")
car2.start_engine()
car2.stop_engine()
