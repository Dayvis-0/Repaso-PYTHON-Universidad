from Progresion import Progresion

class ProgresionAritmetica(Progresion):
    """Iterador que produce una progresion aritmetica"""
    
    def __init__(self, incremento=1, start=0):
        """Crea una nueva progresion aritmetica
        
        incremento  la constante fija para agergar
        star        el primer elemento de la progresion
        """
        super().__init__(start)
        self._incremento = incremento
    
    def _avanza(self):
        """Actualiza el valor actual agregando el incremento"""
        self._actual += self._incremento
