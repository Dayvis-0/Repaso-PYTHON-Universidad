# SortedPriorityQueue  

from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList

class Empty(Exception):
  pass

class SortedPriorityQueue(PriorityQueueBase):
  """Una cola de prioridad orientada a minimo con un lista ordenada"""

  #----------------------------funciones publicas ------------------------------
  def __init__(self):
    """Crea una nueva cola de prioridad."""
    self._data = PositionalList()

  def __len__(self):
    """Devuelve la cantidad de elementos de la cola de prioridad."""
    return len(self._data)

  def add(self, key, value):
    """Agrega un nuevo par clave, valor."""
    newest = self._Item(key, value)             # make new item instance
    walk = self._data.last()       # walk backward looking for smaller key
    while walk is not None and newest < walk.element():
      walk = self._data.before(walk)
    if walk is None:
      self._data.add_first(newest)              # new key is smallest
    else:
      self._data.add_after(walk, newest)        # newest goes after walk

  def min(self):
    """devuelve pero no elimina la tupla (k,v) con el k minimo.

    Origina un error si esta vacia.
    """
    if self.is_empty():
      raise Empty('Cola de prioridad vacia.')
    p = self._data.first()
    item = p.element()
    return (item._key, item._value)

  def remove_min(self):
    """Remueve y devuelve la tupla (k,v) con el k minimo.

    Origina un error si esta vacia.
    """
    if self.is_empty():
      raise Empty('La cola de prioridad esta vacia.')
    p = self._data.first()
    item = p.element()
    self._data.delete(self._data.first())
    return (item._key, item._value)
