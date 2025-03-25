from MapBase import MapBase
from collections import MutableMapping
from random import randrange # Usado para seleccionar parametros MAD 

class HashMapBase(MapBase):
    """ Clase base abstract para un map usando tabla-hash con compresion MAD
    las claves deben ser hashables y no nulas"""

    def __init__(self, cap=11, p = 109345121):
        """Crear una tabal hash map vacia.
        cap     tamaño inicial de la tabla (preterminado 11)
        p       Se utiliza p positivo para MAD (preterminado: 109345121)"""

        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        
        return self._n

    def __getitem__(self, key):
        
        j = self._hash_function(key)

        return self._bucket_getitem(j, key)         # KeyError

    def __setitiem__(self, key, value):
        
        j = self._hash_function(key)
        self._bucket_setitem(j, key, value)         # Mantiene self._n

        if self._n > (len(self._table)) // 2:       # Factor de carga <= 0.5
            self._resize(2 * len(self._table) - 1)  # Numero 2^x - 1 es primo

    def __delitem__(self, k):
        
        j = self._hash_function(k)
        self._bucket_delitem(j, k)                  # KeyError
        self._n -= 1
        
    def _resize(self, c):
        """Redimensiona el arreglo a tamaño c y rehash todo los items"""

        old = list(self.items())        # Usa iteracion para todos los items
        self._table = c * [None]        # Resetea la tabla al tamaño deseado
        self._n = 0                     # n se recalcula
        
        for (k, v) in old:
            self[k] = v                 # Reinserta key-value par