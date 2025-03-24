import heapq as he 

# Proporciona funciones de colas de prioridad - colas de prioridad y monticulos(heaps)
# Proporciona una lista basada en el heap min, donde el elemento mas pequeño siempre esta en la posicion 0

"""Que es un heap? es una estructura de datos especial que satisface la propiedad de heap. En un min heap, el valor del nodo
padre es menor o igual que los valores de sus hijos. En un max heap, es mayor o igual.

Es una estructura de datos que se utiliza para mantener una coleccion de elementos de modo que siempre sea facil
y rapido acceder al menor o al mayor elemento"""

# heapq.heapush(heap, item) - in

heap = [] 

he.heappush(heap,10)
he.heappush(heap,5)
he.heappush(heap,15)

min_elem = he.heappop(heap) # Sacar el menor elemento de la cola 

# Uso de heapq con tuplas 

heap1 = []

he.heappush(heap1,(1,'one'))
he.heappush(heap1,(2,'two'))
he.heappush(heap1,(3,'trhee'))

# Aplicaciones comunes - ordenacion de datos -> k elemntos de mayor a menor y menor a mayor
# heapq.nlargest(k,item)

heap2 = [1,3,2,5,4,10,7,6,8]

mayor_menor = he.nlargest(5,heap2)
menor_mayor = he.nsmallest(5,heap2)

# implementacion de colas de prioridad

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        
    def push(self, item, priority):
        he.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
        
    def pop(self):
        
        return he.heappop(self._queue)[-1]
    
q = PriorityQueue()

q.push('Uno',1)
q.push('Dos',2)
q.push('Tres',3)

# Optimizacion de operaciones 

import itertools as ite 

item1 = [1,3,2]
perms = list(ite.permutations(item1))
he.heapify(perms)

print(perms) 
print(type(perms))