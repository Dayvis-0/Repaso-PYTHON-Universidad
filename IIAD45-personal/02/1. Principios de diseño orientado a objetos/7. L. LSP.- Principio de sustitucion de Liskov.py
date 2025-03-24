"""Liskov Substitucion Principle (LSP)

Principio de sustitucion de Liskov:
Los objetos de una clase derivada deben poder sustituir a los objetos de la clase base sin alterar el comportamiento del programa.
En otras palabras, si tienes una clase base y una clase derivada (subclase), deberias poder usar una instancia de la subclase en
cualquier lugar donde se espera una instancia de la clase base sin que esto cause errores o comportamientos inesperados"""

class Bird:
    def fly(self):
        return 'Flying'
    
class FlyingBird(Bird):
    def fly(self):
        return 'Flying'
    
class NonFlyingBird(Bird):
    def swim(self):
        return 'Swimming'    
    
birds = [FlyingBird(), NonFlyingBird()]

for bird in birds:
    if isinstance(bird, FlyingBird):
        print(bird.fly())
    else:
        print(bird.swim())