# UnsortedPriorityQueue.py Una implementacion de una cola de prioridad usando una lista desordenada

from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList

class UnsortedPriorityQueue(PriorityQueueBase): 
  """Una cola de prioridad orientada a minimo con una lista desordenada"""

  #----------------------------- funciones no publicas --------------------------
  def _find_min(self):
    """Devuelve la posicon del item con la clave minima"""
    if self.is_empty():               # is_empty inherited from base class
      raise Empty('Cola de prioridad vacia')
    small = self._data.first()
    walk = self._data.after(small)
    while walk is not None:
      if walk.element() < small.element():
        small = walk
      walk = self._data.after(walk)
    return small

  #------------------------------ funciones publicas-----------------------------
  def __init__(self):
    """Crea una cola de prioridad nueva y vacia."""
    self._data = PositionalList()

  def __len__(self):
    """Devuelve el numero de elementos de una cola de prioridad."""
    return len(self._data)

  def add(self, key, value):
    """Adiciona un nuevo par clave, valor."""
    self._data.add_last(self._Item(key, value))

  def min(self):
    """Devuelve una tupla (k,v) con el minimo valor pero no la remueve.

    Origina una excepcion Empty.
    """
    p = self._find_min()
    item = p.element()
    return (item._key, item._value)

  def remove_min(self):
    """Remueve y devuelve una tupla (k,v) con el minimo valor k.

    Origina un error si esta vacia.
    """
    p = self._find_min()
    item = p.element()
    self._data.delete(p)
    return (item._key, item._value)