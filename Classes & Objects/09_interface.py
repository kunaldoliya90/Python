# 9.9 Write a python program to demonstrate Interface
from abc import ABC, abstractmethod

# Interface-like abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing the Shape interface
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete class implementing the Shape interface
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create instances of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Display information about shapes
print("Circle - Area:", circle.area(), "Perimeter:", circle.perimeter())
print("Rectangle - Area:", rectangle.area(), "Perimeter:", rectangle.perimeter())
