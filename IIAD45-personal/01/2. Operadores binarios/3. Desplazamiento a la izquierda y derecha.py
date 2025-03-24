class DesplazamientoBinario:
    def __init__(self, numero):
        self._numero = numero
        
    def a_binario(self):
        
        return bin(self._numero)[2:]
    
    def desplazamiento_izquierda(self, posiciones):
        
        des = self._numero << posiciones
        
        return bin(des)[2:] 
    
    def desplazamiento_derecha(self, posiciones):
        
        des = self._numero >> posiciones
        
        return bin(des)[2:]
    
num1 = DesplazamientoBinario(10)

print(num1.a_binario())

print(f'Desplazamiento a la derecha: {num1.desplazamiento_derecha(2)}')
print(f'Desplazamiento a la izquierda: {num1.desplazamiento_izquierda(2)}')