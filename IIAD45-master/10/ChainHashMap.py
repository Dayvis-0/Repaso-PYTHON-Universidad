# Ejemplo 10-5. ChainHashMap

from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap

class ChainHashMap(HashMapBase):
  """map hash implementado con encadenamiento para resolucion de colisiones"""

  def _bucket_getitem(self, j, k):
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error: ' + repr(k))        # no encuentra match
    return bucket[k]                                 # KeyError

  def _bucket_setitem(self, j, k, v):
    if self._table[j] is None:
      self._table[j] = UnsortedTableMap()     # bucket es nuevo a la tabla
    oldsize = len(self._table[j])
    self._table[j][k] = v
    if len(self._table[j]) > oldsize:         # key fue nueva a la tabla
      self._n += 1                            # incrementa el tamano del map

  def _bucket_delitem(self, j, k):
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error: ' + repr(k))        # no hay match
    del bucket[k]                                    # KeyError

  def __iter__(self):
    for bucket in self._table:
      if bucket is not None:                         # un slot no vacio
        for key in bucket:
          yield key
