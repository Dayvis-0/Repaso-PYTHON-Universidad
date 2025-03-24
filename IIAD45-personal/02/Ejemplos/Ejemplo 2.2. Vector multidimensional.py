class Vector:
    """Representa un vector como un espacio multidimensional"""
    def __init__(self, d):
        """Crea un vector d-dimensional de ceros"""
        self._coordinates = [0]*d
        
    def __len__(self):
        """Devuelve la dimension del vector"""
    
        return len(self._coordinates)
    
    def __getitem__(self, i):
        """Devuelve el valor que hay en la coordenada i-esima del vector"""
        
        return self._coordinates[i]
    
    def __setitem__(self, i, value):
        """Establece la coordenada i-esima con un valor"""
        
        self._coordinates[i] = value
        
    def __add__(self, other):
        
        if len(self) != len(other):
            raise ValueError('Las dimensiones de los dos vectores deben de coincidir')
    
        result = Vector(len(self))
        
        for i in range(len(self)):
            result[i] = self[i] + other[i]
            
        return result
    
    def __eq__(self, other):
        """Devuelve True si los dos vectores son iguales, al contrario devuelve False"""
    
        return self._coordinates == other._coordinates
    
    def __ne__(self, other):
        """Devuelve True si los dos vectores son diferentes, al contrario devuelve False"""
        
        return not self == other
    
    def __str__(self):
        
        return f'<{str(self._coordinates)[1:-1]}>'    

vec1 = Vector(2)
vec2 = Vector(2)

vec1[0], vec1[1] = 1, 2
vec2[0], vec2[1] = 3, 4

print(vec1 + vec2)