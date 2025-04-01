"""
Una empresa de tecnología está desarrollando un sistema para gestionar vehículos autónomos. Cada vehículo tiene ciertas características generales
y puede tener diferentes roles dentro del sistema.
Se deben modelar las siguientes clases:

#* 1 Clases Base
    Vehiculo → Representa cualquier vehículo y tiene los atributos:
        marca (Ej: Tesla, BMW)
        modelo (Ej: Model X, i8)
        año (Ej: 2023, 2024)
    Autonomia → Representa la capacidad del vehículo para operar sin intervención humana y tiene los atributos:
        nivel_autonomia (Número del 1 al 5 según su grado de automatización)
        kilometros_restantes (Indica cuántos kilómetros puede recorrer antes de recargar)
#* 2 Clases Derivadas con Herencia Múltiple
    TaxiAutonomo → Hereda de Vehiculo y Autonomia, y tiene los atributos adicionales:
        tarifa_por_km (Costo por kilómetro)
        pasajeros_actuales (Cantidad de pasajeros en el taxi)
    CamionAutonomo → Hereda de Vehiculo y Autonomia, y tiene los atributos adicionales:
        capacidad_carga (Capacidad en toneladas)
        carga_actual (Peso de la carga actual)
#* 3 Requisitos del Programa
    1. Crear una colección de vehículos que incluya varios TaxiAutonomo y CamionAutonomo.
    2. Recorrer la colección con un bucle y, dependiendo del tipo de vehículo:
        Si es un TaxiAutonomo, imprimir su tarifa por km y la cantidad de pasajeros.
        Si es un CamionAutonomo, imprimir su capacidad de carga y la carga actual.
    3. Usar condicionales para evaluar:
        Si el nivel de autonomía es menor o igual a 2, imprimir un mensaje de advertencia: "Nivel de autonomía bajo. Requiere supervisión."
        Si un TaxiAutonomo tiene más de 4 pasajeros, imprimir: "Capacidad máxima alcanzada."
        Si un CamionAutonomo supera su capacidad de carga, imprimir: "¡Sobrecarga detectada!"
        Si el kilometros_restantes es menor a 50, imprimir: "Advertencia: Batería baja, recargar pronto."
    4. Contar cuántos taxis tienen más de 2 pasajeros y cuántos camiones están sobrecargados.
    5. Al final, mostrar un resumen con las estadísticas generales:
        Total de taxis con más de 2 pasajeros.
        Total de camiones sobrecargados.
        Total de vehículos con batería baja.
"""

import time, emoji

class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self._marca = marca
        self._modelo = modelo
        
class Automia:
    def __init__(self, nivel_autonomia: int, kilometros_restantes: float):
        self._nivel_autonomia = nivel_autonomia
        self._kilometros_restantes = kilometros_restantes
        
class TaxiAutonomo(Vehiculo, Automia):
    def __init__(self, marca, modelo, nivel_autonomia, kilometros_restantes, tarifa_por_km: float, pasajeros_actuales: int):
        Vehiculo.__init__(self, marca, modelo)
        Automia.__init__(self, nivel_autonomia, kilometros_restantes)
        self._tarifa_por_km = tarifa_por_km
        self._pasajeros_actuales = pasajeros_actuales
        
class CamionAutonomo(Vehiculo, Automia):
    def __init__(self, marca, modelo, nivel_autonomia, kilometros_restantes, capacidad_carga: int, carga_actual: int):
        Vehiculo.__init__(self, marca, modelo)
        Automia.__init__(self, nivel_autonomia, kilometros_restantes)
        self._capacidad_carga = capacidad_carga
        self._carga_actual = carga_actual
            

vehiculos = [TaxiAutonomo('Tesla', 'BMW', 4, 1500, 6, 2), CamionAutonomo('Bolvo', 'KAw', 1, 1000, 20, 10), 
             CamionAutonomo('Tractor', 'KSA', 2, 1020, 15, 7), TaxiAutonomo('Toyota', 'XVI', 2, 20, 4.5, 3),
             TaxiAutonomo('Samsung', 'YSI', 3, 750, 4, 3), CamionAutonomo('Toyota', '4x4', 1, 900, 18, 12)]

cont_taxi_pasa = 0
cont_cami_sombre = 0
cont_bate_baja = 0

for vehiculo in vehiculos:
    if  isinstance(vehiculo, TaxiAutonomo):
        print('\n\tTaxi Autonomo')
        print(f'La tarifa por kilometro es {vehiculo._tarifa_por_km}\nCantidad de pasajeros: {vehiculo._pasajeros_actuales}')

        if vehiculo._nivel_autonomia <= 2:
            print("Nivel de autonomía bajo. Requiere supervisión.")
        
        if vehiculo._pasajeros_actuales > 4:
            print("Capacidad máxima alcanzada.")
            
        if vehiculo._kilometros_restantes < 50:
            print("Advertencia: Batería baja, recargar pronto.")
            cont_bate_baja += 1
            
        if vehiculo._pasajeros_actuales > 2:
            cont_taxi_pasa += 1
    else:
        print('\n\tCamion Autonomo')
        print(f'Capacidad de carga: {vehiculo._capacidad_carga}\nCarga actual: {vehiculo._carga_actual}')
        if vehiculo._nivel_autonomia <= 2:
            print(":warning: Nivel de autonomía bajo. Requiere supervisión.")
            
        if vehiculo._carga_actual > vehiculo._capacidad_carga:
            print("¡Sobrecarga detectada!")
            cont_cami_sombre += 1
            
        if vehiculo._kilometros_restantes < 50:
            print("Advertencia: Batería baja, recargar pronto.")
            cont_bate_baja += 1
            
    time.sleep(2)
            
print(f"""\nTotal de taxis con más de 2 pasajeros: {cont_taxi_pasa}
Total de camiones sobrecargados: {cont_cami_sombre}
Total de vehículos con batería baja: {cont_bate_baja}""")