#Ejemplo 10-4. MapBase

from MapBase import MapBase
from collections import MutableMapping
from random import randrange         # used to pick MAD parameters

class HashMapBase(MapBase):
  """  Clase base abstracta para un map usando tabla-hash con compresion MAD

  las claves deben ser hashables y no nulas.
  """

  def __init__(self, cap=11, p=109345121):
    """Crea una tabla hash map vacia.

    cap     initial table size (default 11)
    p       positive prime used for MAD (default 109345121)
    """
    self._table = cap * [ None ]
    self._n = 0                                   # cantidad de entradas
    self._prime = p                               # primo para compresion MAP
    self._scale = 1 + randrange(p-1)              # escala 1 to p-1 para MAD
    self._shift = randrange(p)                    # despl de 0 to p-1 para MAD

  def _hash_function(self, k):
    return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

  def __len__(self):
    return self._n

  def __getitem__(self, k):
    j = self._hash_function(k)
    return self._bucket_getitem(j, k)             # KeyError

  def __setitem__(self, k, v):
    j = self._hash_function(k)
    self._bucket_setitem(j, k, v)                 # mantiene self._n
    if self._n > len(self._table) // 2:           # factor de carga <= 0.5
      self._resize(2 * len(self._table) - 1)      # numero 2^x - 1 es primo

  def __delitem__(self, k):
    j = self._hash_function(k)
    self._bucket_delitem(j, k)                    # KeyError
    self._n -= 1

  def _resize(self, c):
    """Redimensiona el arreglo a tamano c y rehash todos los items"""
    old = list(self.items())       # usa iteracion para los items
    self._table = c * [None]       # resetea la tabla al tam deseado
    self._n = 0                    # n se recalcula
    for (k,v) in old:
      self[k] = v                  # reinserta key-value par
