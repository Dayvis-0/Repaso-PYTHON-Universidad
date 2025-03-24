"""La herencia permite crear una nueva clase basada en un clase existente, reutilizando su comportamiento y reutilizandodlo"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def description(self):
        return f'Brand: {self.brand}\nModel: {self.model}'
    
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand,model)
        self.num_doors = num_doors
        
    def description(self):
        return f'\tCar\n{super().description()}\nWhit: {self.num_doors} doors'
    
car = Car('Toyota','Carolla',4)

print(car.description())