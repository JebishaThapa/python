#inheritance = allows a class to inherit attributes and methods for another class

#multiple inheritance = inherit from more than one parent 
#abstarct class : a class trhat xannot ber instanitiated on tis own, meant to be subclassed

#super() = functio used in a child class to call methods from a parent class (super class).
#allows you to extend the functionality of thr inherited methids


class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
     
        self.radius = radius

class Square:
    def __init__(self, color, filled, width):
        self.color = color
        self.filled = filled
        self.width = width
    
circle = Circle(color="red", filled=True, radius = 5)

print(circle.color)