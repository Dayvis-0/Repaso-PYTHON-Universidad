# Ejemplo 5-9. Una clase para el cifrador Cesar

class CifradorCesar:
    """Clase para hacer cifrado y descifrado usando cifrado Cesar"""
    
    def __init__(self, desp):
        """Construye el cifrado usando desp como rotacion"""
        encoder = [None]*26
        decoder = [None]*26
        for k in range(26):
            encoder[k] = chr((k + desp)%26 + ord('A'))
            decoder[k] = chr((k - desp)%26 + ord('A'))
        self._adelante = ''.join(encoder)
        self._atras    = ''.join(decoder)
        
    def encripta(self, mensaje):
        """Devuelve una cadena con el mensaje cifrado"""
        return self._transform(mensaje, self._adelante)
    
    def desencripta(self, secreto):
        """Devuelve el mensaje descifrado"""
        return self._transform(secreto, self._atras)
    
    def _transform(self, original, code):
        """Realizar la transformacion en base a una cadena"""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)
    
if __name__ == '__main__':
    cifrador = CifradorCesar(7)
    mensaje = "Hola"
    codificado = cifrador.encripta(mensaje)
    print('Secret: ', codificado)
    respuesta = cifrador.desencripta(codificado)
    print('Mensaje: ', respuesta)
    
