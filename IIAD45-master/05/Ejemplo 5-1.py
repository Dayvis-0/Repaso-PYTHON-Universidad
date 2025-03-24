# Ejemplo 5-1. Experimento para ver la relacion entre una lista y su arreglo

import sys
data = []
for k in range(100):
    a = len(data)
    b = sys.getsizeof(data)
    print('Longitud: {0:3d}; Tamano en bytes: {1:4d}'.format(a,b))
    data.append(None)