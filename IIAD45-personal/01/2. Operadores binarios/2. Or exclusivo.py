class NumeroBinarioXOR:
    def __init__(self, num1, num2):
        self._numero_1 = num1
        self._numero_2 = num2
        
    def a_binario(self):
        
        return (bin(self._numero_1)[2:],bin(self._numero_2)[2:])
    
    def xor(self):
        
        orexc = self._numero_1 ^ self._numero_2
    
        return bin(orexc)[2:]
    
bin1 = NumeroBinarioXOR(10,12)

print(bin1.a_binario())

print(bin1.xor())