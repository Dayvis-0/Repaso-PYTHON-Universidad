from ArregloDinamico import ArregloDinamico

class Arreglo(ArregloDinamico):
    
    def insert(self, k, valor):
        """Inserta el valor en el indice k, desplazando valores a la derecha"""
        
        self._comp_dimen()
            
        for i in range(self._n, k, -1):
            self._A[i] = self._A[i-1]
            
        self._A[k] = valor
        self._n += 1
        
arr2 = Arreglo()

arr2.append(1)
arr2.append(2)

print(arr2)

arr2.insert(0,0)

print(arr2)