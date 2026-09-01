# SOLID PRINCIPLES

# SINGLE RESPONSIBILITY

from math import pi 
from pathlib import Path
from zipfile import ZipFile 
from abc import ABC, abstractmethod

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)
    def write(self, data, encoding="utf-8"):
        return self.path.write_text(data, encoding)

class ZipfileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix('.zip'), mode="w") as archive:
            archive.write(self.path)
    
    def decompress(self):
        with ZipFile(self.path.with_suffix('.zip'), mode="r") as archive:
            archive.extractall()
    
# OPEN-CLOSED PRINCIPLE
# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "cirle":
            self.radius = kwargs["radius"]
        else:
            raise TypeError("Un supported shape_type")

    def calculateArea(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius ** 2
        else:
            raise TypeError("Un-supported shape type")

rectangle = Shape("rectangle", width=10, height=5)
print(rectangle.calculateArea())


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type
    
    @abstractmethod
    def calculateArea(self):
        print('calling main function only')
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculateArea(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
    
    def calculateArea(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side
    def calculateArea(self):
        return self.side ** 2

r = Rectangle(4, 5)
s = Square(5)
print(r.calculateArea())
print(s.calculateArea())


# LISKOV Substitution Principle (LSV)
# Subtypes must be substitutable for  their base types
