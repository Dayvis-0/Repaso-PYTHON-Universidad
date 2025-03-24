class Vector:
    """Representa un vector como un espacio multidimensional"""
    
    def __init__(self, d):
        """crea un vector d-dimensional de ceros"""
        self._coordenadas = [0] * d
        
    def __len__(self):
        """devuelve la dimension del vector"""
        return len(self._coordenadas)
    
    def __getitem__(self, j):
        """Devuelve la coordenada j-esima del vector"""
        return self._coordenadas[j]
    
    def __setitem__(self, j, val):
        """Establece la j-esima cooredenada con un valor"""
        self._coordenadas[j] = val
        
    def __add__(self, otro):
        """Devuelve la suma de dos vectores"""
        if len(self) != len(otro):
            raise ValueError('Dimensiones deben coincidir')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + otro[j]
        return result
            
    def __eq__(self, otro):
        "devuelve si dos vectores son iguales"
        return self._coordenadas == otro._coordenadas
    
    def __ne__(self, otro):
        "Devuelve True si el vector es distinto del otro"
        return not self == otro
    
    def __str__(self):
        "Produce una representacion en string del vector"
        return '<' + str(self._coordenadas)[1:-1] + '>'
