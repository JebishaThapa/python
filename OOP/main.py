#inheritance = allows a class to inherit attributes and methods for another class

#multiple inheritance = inherit from more than one parent 
#abstarct class : a class trhat xannot ber instanitiated on tis own, meant to be subclassed

#super() = functio used in a child class to call methods from a parent class (super class).
#allows you to extend the functionality of thr inherited methids

"""
polymorphism = greek word means to have many forms or faces
poly = many
morphe = form 
"""
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius ** 2
        

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5 



shapes = [Circle(4), Square(5), Triangle(6, 7)]

for shape in shapes:
    print(f"{shape.area()} cm square.")