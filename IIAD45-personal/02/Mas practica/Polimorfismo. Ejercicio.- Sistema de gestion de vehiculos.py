"""
Una empresa de estacionamientos quiere desarrollar un sistema para gestionar los vehículos que ingresan y salen. Para esto, se 
debe implementar un sistema utilizando polimorfismo, condicionales, ciclos y colecciones.

#*  Vehículos:
    Hay tres tipos de vehículos: Autos, Motos y Camiones.
    Todos los vehículos comparten atributos básicos como placa, hora de entrada y tarifa base.
    Cada tipo de vehículo tiene una tarifa específica:
        Autos: Tarifa base * 1
        Motos: Tarifa base * 0.5
        Camiones: Tarifa base * 2
#* Registro de vehículos:
    Se debe utilizar una colección (lista, diccionario, etc.) para almacenar los vehículos que están en el estacionamiento.
#* Salida y cálculo de tarifa:
    Cuando un vehículo sale, se debe registrar la hora de salida y calcular el costo total basado en el tiempo que estuvo estacionado.
    Si el vehículo estuvo menos de una hora, se cobra la tarifa mínima.
    Si el vehículo estuvo más de 5 horas, se aplica un descuento del 10% sobre la tarifa total.
#* Reglas adicionales:
    El sistema debe validar que un vehículo con la misma placa no se registre dos veces en el estacionamiento.
    Si un vehículo que intenta salir no está registrado, debe mostrar un mensaje de error.
    Debe existir un menú con opciones para registrar entrada, registrar salida, y mostrar la lista de vehículos actualmente estacionados.
"""

from datetime import datetime
import os

class Vehiculos:
    def __init__(self, placa, tarifa_base):
        self._placa = placa
        self._hora_entrada = datetime.now()
        self._tarifa_base = tarifa_base
        
    def calcular_tarifa(self, horas):
        return self._tarifa_base * horas
    
class Auto(Vehiculos):
    def __init__(self, placa):
        super().__init__(placa, tarifa_base = 10)
        
class Moto(Vehiculos):
    def __init__(self, placa):
        super().__init__(placa, tarifa_base = 5)
        
class Caminon(Vehiculos):
    def __init__(self, placa):
        super().__init__(placa, tarifa_base = 20)        

estacionamiento = {}

def registrar_entrada():
    placa = input('Igrese la placa del vehiculo: ')
    tipo = input('Ingrese el tipo de vehiculo (moto/auto/camion): ').lower()

    if placa in estacionamiento:
        return
    
    match (tipo):
        case 'auto':
            estacionamiento[placa] = Auto(placa)
        case 'moto':
            estacionamiento[placa] = Moto(placa)
        case 'camion':
            estacionamiento[placa] = Caminon(placa)
        case _:
            print('El tipo de vehiculo no es valido')
            return

def registrar_salida():
    placa = input('Ingrese la placa del vehiculo que sale: ')
    
    if placa not in estacionamiento:
        print('Este vehiculo no esta en el estacionamiento')
        return

    vehiculo = estacionamiento.pop(placa)
    hora_salida = datetime.now()
    tiempo_estacionado = (hora_salida - vehiculo._hora_entrada).total_seconds() / 1600
    
    if tiempo_estacionado < 1: 
        tiempo_estacionado = 1
        
    costo = vehiculo.calcular_tarifa(tiempo_estacionado)

    if tiempo_estacionado > 5:
        costo *= 0.9

    print(f'Vahiculo {placa} ha salido. Tiempo estacionado: {tiempo_estacionado} horas. Total a pagar {costo}')        

def mostrar_vehiculos():
    if not estacionamiento:
        print('No hay vehiculos en el estacionamiento')
    else:
        print('\tVehiculos en el estacionamiento')
        
        for placa, vehiculo in estacionamiento.items():
            print(f'Placa: {vehiculo._placa}, hora de entrada: {vehiculo._hora_entrada.strftime('%H:%M:%S')}')

def menu():
    
    while True:
        print(f'\n\tMenu\n1. Registrar vehiculo\n2. Registrar salida\n3. Lista de vehiculos\n4. Salir del programa')
        opcion = input('Seleccione una opcion: ')

        match (opcion):
            case '1':
                os.system('cls')
                registrar_entrada()
            case '2':
                os.system('cls')
                registrar_salida()
            case '3':
                os.system('cls')
                mostrar_vehiculos()
            case '4':
                print('Saliendo del programa')
                break
            case _:
                print('Opocion invalida')
                
menu()