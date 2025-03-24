class Progresion:
    """Iterador que produce una progresion generica
    
    el iterador por default produce los numeros 0, 1, 2 ...
    """
    
    def __init__(self, start=0):
        """Inicializa el actual al primer valor de la progresion"""
        self._actual = start
    
    def _avanza(self):
        """Actualiza self._actual a un nuevo valor
        
        Este debe ser sobrecargado por una subclase que personalice 
        la progresion
        
        Por convencion, si actual se establece a None, este senala
        el fin de una progresion finita
        """
        
        self._actual += 1
    
    def __next__(self):
        """Devuelve el siguiente elemento, o si se origina un 
        error StopIteration"""

        if self._actual is None:        
            raise StopIteration()
        else:
            respuesta = self._actual    
            self._avanza()              
            return respuesta            
        
    def __iter__(self):
        """Por convencion un iterador debe devolverse a si mismo 
        como un iterador"""
        return self
    
    def imprimir_progresion(self, n):
        """Imprime los n valores siguientes de la progresion"""
        print(' '.join(str(next(self)) for j in range(n)))