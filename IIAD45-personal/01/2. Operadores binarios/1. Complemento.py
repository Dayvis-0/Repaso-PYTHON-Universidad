class NumeroBinario:
    def __init__(self, nume):
        self._numero = nume 
        
    def a_binario(self):
        
        return bin(self._numero)[2:]
    
    def complemento_binario(self):
        
        comp = ~self._numero
        
        return '-'+str(bin(comp)[3:])
    
num1 = NumeroBinario(10)

print(f'Numero en binario: {num1.a_binario()}')
print(f'Complememnto binario: {num1.complemento_binario()}')