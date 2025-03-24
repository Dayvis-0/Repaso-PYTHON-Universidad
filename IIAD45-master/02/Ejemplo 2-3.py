class IteradorSecuencial:
    """Un iteradora para cualquier tipo secuencial"""
    
    def __init__(self, secuencia):
        """Crea un iterador para la secuencia dada"""
        self._seq = secuencia
        self._k = -1
        
    def __next__(self):
        """Devuelve el siguiente elemento"""
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration
            
    def __iter__(self):
        """Por convencion un iterador debe devolver otro"""
        return self