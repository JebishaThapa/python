class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def introduce(self):
        print(f"I am {self.name}, a {self.age}-year-old {self.breed}.")


dog1 = Dog("Buster", "Golden Retriever", 3)
dog2 = Dog("Luna", "Beagle", 2)

dog1.introduce()
dog1.bark()

dog2.introduce()
print(dog2.name)
