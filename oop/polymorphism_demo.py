import math

class Shape:
    """
    Base class defining the abstract interface for all shapes.
    Subclasses MUST override the area() method.
    """
    def area(self):
        """
        The area calculation method. Raises an error if not implemented by a derived class.
        """
        raise NotImplementedError("Subclass must implement abstract method 'area'")

class Rectangle(Shape):
    """
    Derived class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides Shape.area() to calculate the area: length * width.
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle, inheriting from Shape.
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """
        Overrides Shape.area() to calculate the area: π * radius².
        Uses math.pi for precision.
        """
        return math.pi * (self.radius ** 2)