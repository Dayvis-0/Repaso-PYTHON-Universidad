"""
Eres un desarrollador de software y te han pedido implementar un sistema para gestionar cuentas bancarias. Cada cuenta bancaria debe contener
información privada, como el número de cuenta, el saldo y el nombre del titular. Además, el sistema debe permitir solo ciertas operaciones 
controladas par garantizar la seguridad y eficiencia del acceso a los datos.

Requisitos:
#* Encapsulación de Datos:
    El número de cuenta y el saldo deben estar ocultos y solo accesibles mediante métodos específicos.
    El nombre del titular también debe estar protegido, permitiendo modificaciones controladas.
#* Métodos Permitidos:
    Un método para depositar dinero en la cuenta.
    Un método para retirar dinero, pero solo si hay saldo suficiente.
    Un método para consultar el saldo, sin exponer directamente la variable interna.
    Un método para modificar el nombre del titular, asegurando que no esté vacío.
#* Manejo de Complejidad:
    Espacial: Evita almacenar datos innecesarios y optimiza el uso de memoria.
    Temporal: Asegura que las operaciones de depósito y retiro sean eficientes, con una complejidad cercana a O(1).
#* Prueba de Seguridad:
    Intenta acceder directamente a los atributos privados desde fuera de la clase.
    Verifica que no puedas modificar el saldo sin usar los métodos definidos.
"""

from dataclasses import dataclass

@dataclass
class CuentaBancaria:
    __numero_cuenta: int
    __nomb_titu: str
    __saldo: int = 0
    
    def _negativo(self, dinero):
        
        if dinero < 0:
            return 'No puedes depositar negativo'
    
    def depositar_dinero(self, dinero_depo: int) -> str:
        
        self._negativo(dinero_depo)

        self.__saldo += dinero_depo
        return 'Dinero depositado'
        
    def retirar_dinero(self, cantidad: int) -> str:
        
        self._negativo(cantidad)
        
        if self.__saldo < cantidad:
            return 'No se puede depositar'
        
        self.__saldo -= cantidad
        return 'El retiro fue exitoso'
    
    def consultar_saldo(self) -> int:
        
        return self.__saldo
    
    def modificar_nombre(self, nuevo_nomb: str) -> str:
        
        if len(self.__nomb_titu) <= 0:
            return 'No tiene nombre'

        self.__nomb_titu = nuevo_nomb
        return 'Nombre modificado'
    
    def obtene_numero_cuenta(self) -> int:
        return self.__numero_cuenta

    def obtener_nombre_titular(self) -> str:
        return self.__nomb_titu

cuenta1 = CuentaBancaria(123, 'Dayvis')

print(cuenta1.depositar_dinero(100))
print(cuenta1.retirar_dinero(50))
print(cuenta1.consultar_saldo())
print(cuenta1.obtene_numero_cuenta())
print(cuenta1.obtener_nombre_titular())