# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints

# MEGHA: Import ABC i.e. abstract base class
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return (self.side ** 2)

# MEGHA: Comment below because GraphicShape class cannot be instantiated
# g = GraphicShape()

c = Circle(10)
print("Area of circle: ",c.calcArea())
s = Square(12)
print("Area of square: ",s.calcArea())
