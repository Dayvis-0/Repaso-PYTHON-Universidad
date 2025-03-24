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
    """Return True if the priority queue is empty."""
    return len(self) == 0

  def __len__(self):
    """Return the number of items in the priority queue."""
    raise NotImplementedError('debe ser implementada por la subclase')

  def add(self, key, value):
    """Add a key-value pair."""
    raise NotImplementedError('debe ser implementada por la subclase')

  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    raise NotImplementedError('debe ser implementada por la subclase')

  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    raise NotImplementedError('debe ser implementada por la subclase')
