# Implementacion de la clase Arreglo Dinamico

import ctypes

class ArregloDinamico:
    """Clase arreglo dinamico similar a una lista simplificada"""
    
    def __init__(self):
        self._n = 0
        self._capacidad = 1
        self._A = self._crear_arreglo(self._capacidad)
    
    def __len__(self):
        """Devuelve la cantidad de elementos de un arreglo"""
        
        return self._n
    
    def __getitem__(self, k):
        """Devuele el elemento en el indice k"""
        
        if not 0 <= k < self._n:
            raise IndexError('indice invalido')
        
        return self._A[k]
    
    def append(self, obj):
        """Agrega objeto al final del arreglo"""
        
        self._comp_dimen()

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
    
    def _comp_dimen(self):
        
        if self._n == self._capacidad:
            self._redimensiona(2*self._capacidad)
    
    def __str__(self):
        
        return str([self._A[i] for i in range(self._n)])
