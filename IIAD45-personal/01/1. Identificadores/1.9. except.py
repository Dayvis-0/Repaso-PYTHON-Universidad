# Gesstion de cuentas bancarias

class SaldoInsufienteError(Exception):
    def __init__(self, men = 'Saldo insuficiente para retirar'):
        self.mensaje = men
        
        super().__init__(self.mensaje)

class CantidadNegativaError(Exception):
    def __init__(self, men = 'El dinero no puede ser negativo chibolo'):
        self._mensaje = men

        super().__init__(self._mensaje)
        
class CuentaBancaria:
    def __init__(self, titu, sal):
        self._titular = titu
        self._saldo = sal
        
    def depositar(self, cantidad):
        
        if cantidad < 0:
            raise CantidadNegativaError()
                        
        self._saldo += cantidad
        
        return (f'Se deposito: {cantidad}. Nuevo saldo: {self._saldo}')
        
    def retirar(self, cantidad):
        
        if cantidad < 0:
            raise CantidadNegativaError()
        
        if cantidad > self._saldo:
                
            raise SaldoInsufienteError()
                
        self._saldo -= cantidad
            
        return (f'Se retiro: {cantidad}. Nuevo saldo {self._saldo}')
            
cuen1 = CuentaBancaria('Dayvis', 10)

print(cuen1.depositar(100))
print(cuen1.retirar(10))