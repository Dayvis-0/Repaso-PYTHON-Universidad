from Progresion import Progression

class ArithmeticProgression(Progression):
    """Iterador que produce una progresion aritmetica"""
    
    def __init__(self, increase = 1, start = 0):
        """Crea una nueva progresion aritmetica
        
        incremento la constante fija para agregar
        start el primer elemento de la progresion"""
        super().__init__(start)
        self._increase = increase
        
    def _advance(self):
        """Actualiza el valor actual agregando el incremento"""
        
        self._current += self._increase 
        
if __name__ == '__main__':
    
    arith_progre = ArithmeticProgression(3)

    print(next(arith_progre))
    print(next(arith_progre))