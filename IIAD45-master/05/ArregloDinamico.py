# Ejemplo 5-2. Implementacion de la clase ArregloDinamico

import ctypes

class ArregloDinamico:
    """Clase arreglo dinamico similar a una lista simplificada"""
    
    def __init__(self):
        """Crea un arreglo simple"""
        self._n = 0
        self._capacidad = 1
        self._A = self._crear_arreglo(self._capacidad)
        
    def __len__(self):
        """Devuelve la cantida de elementos del arreglo"""
        return self._n
    
    def __getitem__(self, k):
        """Devuelve el elemento con el indice k"""
        if not 0 <= k < self._n:
            raise IndexError('indice invalido')
        return self._A[k]
    
    def append(self, obj):
        """Agrega objeto al final del arreglo"""
        if self._n == self._capacidad:
            self._redimensiona(2*self._capacidad)
        self._A[self._n] = obj
        self._n += 1
        
    def _redimensiona(self, c):
        """Redimensiona el arreglo a capacidad c"""
        B = self._crear_arreglo(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacidad = c
        
    def _crear_arreglo(self, c):
        """Devuelve un arreglo con capacidad c"""
        return (c*ctypes.py_object)()
    
    def insert(self, k, valor):
        """Inserta el valor en el indice k, desplazando valores a la derecha"""
        if self._n == self._capacidad:
            self._redimensiona(2 * self._capacidad)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = valor
        self._n += 1
        
    def remove(self, value):
        """Remover la primera ocurrencia de value"""
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
                self._n -=1
                if self._capacidad//self._n == 2:
                    self._redimensiona(self._capacidad//2)
                return
        raise ValueError('valor no encontrado')
    
    def __str__(self):
        
        return str([i for i in range(self._n)])

arr1 = ArregloDinamico()

arr1.append(1)

print(arr1)