# Ejemplo 5-6. Codigo fuente de la clase EntradaJuego

class EntradaJuego: #EntradaJuego.py
    """Representa una entrada de una lista de puntajes altos"""
    
    def __init__(self, nombre, puntos):
        self._nombre = nombre
        self._puntos = puntos
        
    def get_name(self):
        return self._nombre
    
    def get_puntos(self):
        return self._puntos
    
    def __str__(self):
        return '({0}, {1})'.format(self._nombre, self._puntos)
    
