class Progression:
    """Iterador que produce una progresion generica 
    el iterador por default produce los numero 0, 1, 2..."""
    
    def __init__(self, start = 0):
        """Inicializa el actual al primer valor de la progresion"""
        
        self._current = start
        
    def _advance(self):
        """Actualiza self._current a un nuevo valor
        
        Esto debe ser sobrecargado por una subclase que personalice la progresion
        
        Por convencion, si current se establece aa None, este señala el fin de una progresion finita"""
        
        self._current += 1
        
    def __next__(self):
        """Devuelve el siguiente elemento, o si se origina un error StopIteration"""
        
        if self._current is None:
            raise StopIteration()
        
        else:
            answer = self._current
            self._advance()
            
            return answer
        
    def __iter__(self):
        """Por convencion un iterador debe devolver a si mismo como un iterador"""
        
        return self
    
    def print_progression(self, n):
        """Imprime los n valores siguientes de la progresion"""
        
        print(' '.join(str(next(self)) for _ in range(n)))
        
if __name__ == '__main__':
    
    progre = Progression()

    print(next(progre))
    print(next(progre))
    print(next(progre))
    print(next(progre))

    progre.print_progression(2)