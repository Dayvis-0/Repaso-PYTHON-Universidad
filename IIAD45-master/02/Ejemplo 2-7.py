from Progresion import Progresion

class ProgresionGeometrica(Progresion):
    """Iterador que produce una progresion geometrica"""
    
    def __init__(self, base=2, start=1):
        """Crea una nueva progresion geometrica
        
        incremento  la constante fija que se multiplica
        star        el primer termino de la progresion
        """
        super().__init__(start)
        self._base = base
    
    def _avanza(self):
        """Actualiza el valor actual agregando el incremento"""
        self._actual *= self._base
