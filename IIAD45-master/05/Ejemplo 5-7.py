# Ejemplo 5-7. La clase TablaPuntos

from EntradaJuego import EntradaJuego

class TablaPuntos:
    """Representa una entrada de una lista de puntajes altos"""
    
    def __init__(self, capacidad = 10):
        """Inicializa el tablero con una capacidad maxima dada
        
        Todas las entradas inicialmente son None"""
        self._tablero = [None]*capacidad
        self._n = 0
        
    def __getitem__(self, k):
        """Devuelve un entero en el indice k"""
        return self._tablero[k]
    
    def __str__(self):
        """Devuelve una cadena que representa la lista de puntajes altos"""
        return '\n'.join(str(self._tablero[j]) for j in range(self._n))
    
    def agregar(self, entrada):
        """Considera agregar una entrada a los puntajes altos"""
        puntos = entrada.get_puntos()
        
        #Si el tablero no esta lleno o si la entrada es mayor que la ultima 
        entra = self._n < len(self._tablero) or \
                puntos > self._tablero[-1].get_puntos()
                
        if entra:
            if self._n < len(self._tablero):
                self._n += 1
                
            j = self._n - 1
            while j>0 and self._tablero[j-1].get_puntos()<puntos:
                self._tablero[j] = self._tablero[j-1]
                j -= 1
            self._tablero[j] = entrada
            
if __name__ == '__main__': 
    t = TablaPuntos(5)
    t.agregar(EntradaJuego('ivan',90))
    t.agregar(EntradaJuego('bety',95))
    print(t)