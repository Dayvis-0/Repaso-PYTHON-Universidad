"""Open/Closed Principle (OCP)

Principio de Abierto/Cerrado:
Las entidades de software (clases, modulos, funciones) deben estar abiertas para extension pero cerradas para modificaicon
En otras palabras, el comportamiento de una clase o modulo debe poder extenderse sin necesidad de modificar su codigo fuente existente """

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14*self.radius**2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
shapes = [Circle(2), Rectangle(2,2)]

for shape in shapes:
    print(f'Area: {shape.area()}')