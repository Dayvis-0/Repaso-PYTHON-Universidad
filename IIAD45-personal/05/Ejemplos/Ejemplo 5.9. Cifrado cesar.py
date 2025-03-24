# Implementacion del cifrado Cesar

class CifradoCesar:
    """Construye para hacer cifrado y descifrado con cifrado cesar"""
    
    def __init__(self, desp):
        """Construye el cifrado usando desp como rotacion"""
        
        encoder = [None]*26 
        decoder = [None]*26 
        
        for j in range(26):
            encoder[j] = chr((j + desp)%26 + ord('A'))
            decoder[j] = chr((j - desp)%26 + ord('A'))
            
        self._adelante = ''.join(encoder)
        self._atras = ''.join(decoder)
        
    def encripta(self, mensaje):
        """Devuelve una cadena con el mensaje cifrado"""
        
        return self._transform(mensaje, self._adelante)
    
    def desencripta(self, secreto):
        """Devuelve el mensaje descifrado"""
        
        return self._transform(secreto, self._atras)
    
    def _transform(self, original, code):
        """Realiza la transformacion en base a una cadena"""
        
        msg = list(original)
        
        for j in range(len(msg)):
            
            if msg[j].isupper():
                k = ord(msg[j]) - ord('A')
                msg[j] = code[k]
                
        return ''.join(msg)
    
cifra = CifradoCesar(2)

codi = cifra.encripta('H')
decodi = cifra.desencripta(codi)

print('Codificado: ',codi)
print('Decodificado: ',decodi)