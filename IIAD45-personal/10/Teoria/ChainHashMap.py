# Ejemplo 10-5 ChainHashMap

from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap

class ChainsHashMap(HashMapBase):
    """Map hash implementado con encadenamiento para resolucion de colisiones"""

    def _bucket_getitem(self, j, k):
        
        bucket = self._table[j]

        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))         # no encuenntra match

        return bucket[k]                                    # KeyError

    def _bucket_setitem(self, j, k, v):
        
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()     # bucket es nuevo a la tabla
        
        oldsize =len(self._table[j])
        self._table[j][k] = v
        
        if len(self._table[j]) > oldsize:           # Key fue nueva a la tabla
            self._n += 1                            # Imcrementa el tamaño del map
            
    def _bucket_delitem(self, j, k):
        
        bucket = self._table[j]

        if bucket is None:                                  # No hay match
            raise KeyError('Key Error: ' + repr(k))         # KeyError

        del bucket[k]                                       

    def __iter__(self):
        
        for bucket in self._table:
            if bucket is not None:                          # Un slot no vacio
                for key in bucket:
                    yield key
                    

# Crear una tabla hash con encadenamiento
mapa = ChainsHashMap()

# Insertar valores
mapa["nombre"] = "Alice"
mapa["edad"] = 25
mapa["ciudad"] = "Madrid"

# Acceder a valores
print(mapa["nombre"])  # Output: Alice
print(mapa["edad"])    # Output: 25

# Modificar un valor
mapa["edad"] = 26
print(mapa["edad"])    # Output: 26

# Eliminar un elemento
del mapa["ciudad"]

# Verificar si una clave está en el mapa
print("ciudad" in mapa)  # Output: False

# Iterar sobre las claves
for clave in mapa:
    print(clave, "->", mapa[clave])
