# Codigo fuente de la clase EntradaJuego

class EntradaJuego:
    """Representa una entrada de una lista de puntajes altos"""
    
    def __init__(self, nombre, puntos):
        self._nombre = nombre
        self._puntos = puntos
        
    def get_nombre(self):
        return self._nombre
    
    def get_puntos(self):
        return self._puntos
    
    def __str__(self):
        return '({0},{1})'.format(self._nombre, self._puntos)