# Ejemplo 5-5. Implementando remove para la clase ArregloDinamico

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
    
