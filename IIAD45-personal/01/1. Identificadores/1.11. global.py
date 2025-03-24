# Contador global

contador_global = 0

class ContadorGlobal:
    def __init__(self):
        self._contador = 0
        
    def incrementar(self):
        
        global contador_global
        self._contador += 1
        contador_global += 1
        
    def mostrar(self):
        
        return (f'Valor del contador da la instancia: {self._contador}\nValor del contador global: {contador_global}')
    
    
cont1 = ContadorGlobal()

cont1.incrementar()

print(cont1.mostrar())

cont1.incrementar()
cont1.incrementar()
cont1.incrementar()
cont1.incrementar()
cont1.incrementar()

print(cont1.mostrar())