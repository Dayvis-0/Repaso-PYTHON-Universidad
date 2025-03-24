import math

class Vector:
    def __init__(self, d):
        self._coordinates = [0]*d
        
    def __add__(self, other):
        "Sumar cada elemento de un vector con cada elemento de otro vector"
          
        self._check_dimensions(other)

        addition = Vector(len(self))

        for i in range(len(self)):
            addition[i] = self[i] + other[i]
        
        return addition
    
    def __sub__(self, other):
        "Restar cada elemento de un vector con cada elemento de otro vector"
        
        self._check_dimensions(other)
        
        subtract = Vector(len(self))

        for i in range(len(self)):
            subtract[i] = self[i] - other[i]

        return subtract

    def __mul__(self, other):
        "Multiplicar cada elemento de un vector con cada elemento de otro vector"
        
        self._check_dimensions(other)
        
        multiplication = Vector(len(self))

        for i in range(len(self)):
            multiplication[i] = self[i] * other[i]

        return multiplication
        
    def __truediv__(self, other):
        "DIvidir cada elemento de un vector con cada elemento de otro vector"
        
        for i in other:
            if i == 0:
                raise ValueError('No se puede dividir por cero')
        
        self._check_dimensions(other)
        
        division = Vector(len(self))

        for i in range(len(self)):
            division[i] = self[i] / other[i]

        return division   
    
    def __pow__(self, other):
        "Elevar cada elemento de un vector con cada elemento de otro vector"
        
        self._check_dimensions(other)
        
        power = Vector(len(self))

        for i in range(len(self)):
            power[i] = self[i] ** other[i]

        return power
    
    def __iadd__(self, other):
        "Sumar un vector con asignacion aumentada con otro vector"
        
        for i in range(len(self)):
            self[i] += other[i]   

        return self
    
    def __isub__(self, other):
        "Restar un vector con asignacion aumentada con otro vector"
        
        for i in range(len(self)):
            self[i] -= other[i]   

        return self
    
    def __imul__(self, other):
        "Multiplicar un vector con asignacion aumentada con otro vector"
    
        for i in range(len(self)):
            self[i] *= other[i]   

        return self
    
    def __neg__(self):
        "Hace que cada elemento del vector se multiplique por -1"

        neg_vector = Vector(len(self))

        for i in range(len(self)):
            
            neg_vector[i] = -1 * self[i]

        return neg_vector
    
    def __pos__(self):
        "Hace que cada elemento del vector se multiplique por +1"
        
        pos_vector = Vector(len(self))

        for i in range(len(self)):
            
            pos_vector[i] = +1 * self[i]

        return pos_vector
    
    def __lt__(self, other):
        "compara si el primer vector es menor que el segundo vetor"
        
        self._check_dimensions(other)

        return self._coordinates < other._coordinates
    
    def __le__(self, other):
        "compara si cada elemento del primer vector es menor o igual que cada elemento del segundo vetor"
        
        self._check_dimensions(other)
        
        return self._coordinates <= other._coordinates
    
    def __gt__(self, other):
        "compara si cada elemento del primer vector es mayor que cada elemento del segundo vetor"
        
        return  self._coordinates > other._coordinates
    
    def __ge__(self, other):   
        "compara si cada elemento del primer vector es mayor o igual que cada elemento del segundo vetor"
    
        return self._coordinates >= other._coordinates

    def __eq__(self, other):
        "compara si cada elemento del primer vector es igual a cada elemento del segundo vetor"
        
        return self._coordinates == other._coordinates
    
    def __neg___(self, other):
        "compara si cada elemento del primer vector es diferente que a elemento del segundo vetor"
        
        return self._coordinates != other._coordinates 
    
    def __contains__(self, value):
        "Comprueba si hay un valor en la lista"
        
        return value in self._coordinates
    
    def __getitem__(self, i): # get item -> Obtener articulo
        
        if i > len(self._coordinates) or i <= -1*len(self._coordinates):
            raise ValueError('El indice no esta en el rango')
        
        return self._coordinates[i]
    
    def __setitem__(self, i, value): # set item -> Elemento establecido
        
        if i > len(self._coordinates) or i <= -1*len(self._coordinates):
            raise ValueError('El indice no esta en el rango')
        
        if not isinstance(value,(float,int)):
            raise ValueError('El valor para el vector debe de ser un numeor entero o flotante')
        
        self._coordinates[i] = value
        
    def __len__(self):
        
        return len(self._coordinates)
    
    def _check_dimensions(self, other):
        
        if len(self) != len(other):
            raise ValueError('Las dimensiones deben de ser iguales')
        
    def __str__(self):
        "Muestra el vector"
        
        return '<'+str(self._coordinates)[1:-1]+'>'
        
vec1 = Vector(3)
vec2 = Vector(3)

vec1[0], vec1[1], vec1[2] = 'HOOAL', 2, 3
vec2[0], vec2[1], vec2[2] = 4, 5, 6

print(f'Addtion: {vec1 + vec2}')
print(f'Substract: {vec1 - vec2}')
print(f'Multiplication: {vec1 * vec2}')
print(f'Divison: {vec1 / vec2}')
print(f'Poower: {vec1 ** vec2}')
#vec1 += vec2
#print(f'Increased sum: {vec1}')
#vec1 -= vec2
#print(f'Augmented substraction: {vec1}')
#vec1 *= vec2
#print(f'Augmented multiplication: {vec1}')
print(f'Negative: {-vec1}')
print(f'Positive: {+vec2}')
print(f'Less than: {vec1 < vec2}')
print(f'Less than equal: {vec1 <= vec2}')
print(f'Greater than : {vec1 > vec2}')
print(f'Greater than equal: {vec1 >= vec2}')
print(f'En: {1 in vec1}')
print(f'Search for value: {vec1[0]}')
print(f'Lenght: {len(vec1)}')