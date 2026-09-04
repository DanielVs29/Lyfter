from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


circle = Circle(5)
square = Square(4)
rectangle = Rectangle(10, 5)

print("Circulo")
print("Area:", circle.calculate_area())
print("Perimetro:", circle.calculate_perimeter())

print("\nCuadrado")
print("Area:", square.calculate_area())
print("Perimetro:", square.calculate_perimeter())

print("\nRectangulo")
print("Area:", rectangle.calculate_area())
print("Perimetro:", rectangle.calculate_perimeter())