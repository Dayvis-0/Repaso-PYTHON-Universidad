"""La abstraccion consiste en ocultar la complejidad interna y mostrar solo la funcionalidad esencial."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    
    def make_sound(self):
        return 'Woof'
    
class Cat(Animal):
    
    def make_sound(self):
        return 'Miaun'
    
animals = [Dog(),Cat()]

for animal in animals:
    print(animal.make_sound())