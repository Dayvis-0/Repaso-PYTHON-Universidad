# Implementacion de remove para la clase ArregloDinamico

from ArregloDinamico import ArregloDinamico

class Arreglo(ArregloDinamico):
    
    def remove(self, value):
        """Remueve la primera ocurrencia de value"""
        
        for i in range(self._n):
            
            if self._A[i] == value:
                
                for j in range(i, self._n - 1):
                    self._A[j] = self._A[j+1]
                    
                self._A[self._n-1] = None
                self._n -= 1   
                
                if self._capacidad//self._n == 2:
                    self._redimensiona(self._capacidad//2) 
                
                return
            
        raise ValueError('Valor no encontrado')
    
arr1 = Arreglo()

arr1.append(1)
arr1.append(2)

print(arr1)

arr1.remove(2)

print(arr1)