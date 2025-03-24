class IteradorSecuencial:
    """Un iterador para cualquier tipo secuencia"""
    
    def __init__(self, sequence):
        """Crea un iterador para la secuencia dada"""
        self._sequence = sequence
        self._k = -1
        
    def __next__(self):
        """Devuelve el siguiente elemento"""
       
        self._k += 1
        
        if self._k < len(self._sequence):
            return (self._sequence[self._k])
        
        else:
            raise StopIteration
        
    def __iter__(self):
        """Por convencion un iterador debe devolver otro"""
    
        return self
    
iteseq = IteradorSecuencial([1,2,3])

print(next(iteseq))