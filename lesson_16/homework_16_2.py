from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rhombus(Shape):
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def area(self):
        return (self.side_a ** 2) * math.sin(math.radians(self.angle_a))

    def perimeter(self):
        return self.side_a * 4


class IsoscelesTrapezoid(Shape):

    def __init__(self, side_a, side_b, height):
        self.side_a = side_a
        self.side_b = side_b
        self.height = height

    def area(self):
        return ((self.side_a + self.side_b) / 2) * self.height

    def perimeter(self):
        return self.side_a + self.side_b + 2 * math.sqrt(((self.side_b - self.side_a) / 2) ** 2 + self.height ** 2)

class IsoscelesTriangle(Shape):

    def __init__(self, side_a, side_l):
        self.side_a = side_a
        self.side_l = side_l

    def area(self):
        return 0.5 * self.side_a * math.sqrt(self.side_l ** 2 - (self.side_a / 2) ** 2)

    def perimeter(self):
        return self.side_l * 2 + self.side_a


shapes = [
    Rhombus(5, 60),
    Rhombus(8, 45),
    IsoscelesTrapezoid(5, 8, 4),
    IsoscelesTrapezoid(7, 10, 6),
    IsoscelesTriangle(4, 6),
    IsoscelesTriangle(3, 5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}; Perimeter = {shape.perimeter():.2f}")