"""Eres un desarrollador de software y te han pedido diseñar un sistema que maneje diferentes tipos de vehículos. Cada 
vehículo tiene característicascomunes, pero su funcionamiento puede variar según el tipo (autos, motos, camiones, etc.).

Requisitos:
#* Abstracción de una clase base:
    Debes crear una clase base "Vehiculo" con atributos esenciales como marca, modelo y velocidad actual.
    Define métodos generales como acelerar, frenar y mostrar información.
#* Clases Derivadas:
    Crea al menos dos clases que hereden de "Vehiculo" (por ejemplo, "Auto" y "Moto").
    Cada una debe tener atributos o métodos específicos.
#* Uso de Métodos Abstractos:
    La clase base debe contener al menos un método abstracto, como tipo_vehiculo(), que cada clase hija debe
    implementar de manera diferente.
#* Manejo de Complejidad:
    Espacial: Evita almacenar información redundante.
    Temporal: Asegura que las operaciones como acelerar y frenar sean eficientes (O(1)).
#* Prueba del Sistema:
    Crea instancias de las clases derivadas y prueba sus métodos.#
    Usa polimorfismo llamando a los métodos desde una referencia de la clase base.
"""

import os, time

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    
    def __init__(self, marca: str, modelo: str, velocidad: int = 0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
    
    @abstractmethod
    def tipo_vehiculo():
        pass
    
    def acelerar(self, incremento: int) -> str:
        
        if incremento < 0:
            return 'No se puede acelerar en negativo chibolo'

        self.velocidad += incremento
        return f'{self.tipo_vehiculo()} acelero a {self.velocidad} km/h'

    def frenar(self, decremento: int) -> str:
        
        if decremento < 0:
            return 'No se puede frenar en negativo'
        
        self.velocidad = max(0, self.velocidad - decremento)
        return f'{self.tipo_vehiculo()} redujo la velocidad a {self.velocidad} km/h'

    def mostrar_informacion(self) -> str:
        
        return f"""La marca es: {self.marca}, Velocidad: {self.velocidad}\n"""

class Auto(Vehiculo):
    def tipo_vehiculo(self) -> str:
        return 'Auto'

class Moto(Vehiculo):
    def tipo_vehiculo(self) -> str:
        return 'Moto'         

def menu(classe: object):
    
    while True:
        
        print("""1. Acelerar\n2. Frenar\n3. Mostrar informacion\n4. Salir del programa""")
        resp = int(input('Numero de la accion a hacer: '))

        match resp:
            case 1:
                cuanto1 = int(input('Cuanto? '))
                time.sleep(1)
                os.system('cls')
                print(classe.acelerar(cuanto1))
            case 2:
                cuanto2 = int(input('Cuanto? '))
                time.sleep(1)
                os.system('cls')
                print(classe.frenar(cuanto2))
            case 3:
                time.sleep(1)
                os.system('cls')
                print(classe.mostrar_informacion())
            case 4:
                break
            case _:
                time.sleep(1)
                os.system('cls')
                print('Tiene que ingresar uno de los numeros')
    

print('Vehiculo a seleccinar?\n1. Auto\n2. Moto')
sele = int(input('Numero del vehiculo a seleccionar: '))
auto1 = Auto("Toyota", "Corolla", 100)
moto1 = Moto('Yamaha', 'Carrolla', 100)

if sele == 1:
    menu(auto1)
elif sele == 2:
    menu(moto1)
else:
    print('Debe de ser uno de los numeros')