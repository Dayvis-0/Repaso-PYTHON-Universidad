from Progresion import Progression

class GeometricProgression(Progression):
    """Iterador que produce una progresion geometrica"""
    
    def __init__(self, base = 2, start = 1):
        """Crea una nueva progresion geometrica 
        
        Incremento la constante fija que se multiplica
        star       el primer termino de la progresion"""
        super().__init__(start)
        self._base = base
        
    def _advance(self):
        """Actualiza el valor agregando el incremento"""

        self._current *= self._base
        
if __name__ == '__main__':
    
    geom_progre = GeometricProgression()
    
    print(next(geom_progre))
    print(next(geom_progre))
    print(next(geom_progre))