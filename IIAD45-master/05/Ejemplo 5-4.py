# Ejemplo 5-4. Implementacion de insert de la clase ArregloDinamico

def insert(self, k, valor):
    """Inserta el valor en el indice k, desplazando valores a la derecha"""
    
    if self._n == self._capacidad:
        self._redimensiona(2 * self._capacidad)
    for j in range(self._n, k, -1):
        self._A[j] = self._A[j-1]
    self._A[k] = valor
    self._n += 1
    
    