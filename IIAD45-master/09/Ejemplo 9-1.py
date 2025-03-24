# Ejemplo 9-1. Una clase PriorityQueueBase con una clase anidada _Item


class PriorityQueueBase:
  """Clase base abstracta para una cola de prioridad"""

  #--------------------------- clase anidada _Item ------------------------------
  class _Item:
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __lt__(self, other):
      return self._key < other._key

    def __repr__(self):
      return '({0},{1})'.format(self._key, self._value)

  #-------------------------- funcionalidad publica------------------------------
  def is_empty(self):                 
    """Devuelve True si la cola de prioridad esta vacia."""
    return len(self) == 0

  def __len__(self):
    """Devuelve la cantidad de elementos en una cola de prioridad."""
    raise NotImplementedError('debe ser implementada por la subclase')

  def add(self, key, value):
    """Add a key-value pair."""
    raise NotImplementedError('debe ser implementada por la subclase')

  def min(self):
    """Devuelve pero no remueve la tupla (k,v) con la clave k minima.

    origina un error si esta vacia.
    """
    raise NotImplementedError('')

  def remove_min(self):
    """Remueve y devuelve la tupla (k,v) con el minimo valor de k.

    origina un error si esta vacia.
    """
    raise NotImplementedError('debe ser implementada por la subclase')
