#inheritance = allows a class to inherit attributes and methods for another class

class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

class Dog(animal):
    pass    

class Cat(animal):
    pass

class Mouse(animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfeild")

print(dog.name)
print(dog.is_alive)
dog.eat()