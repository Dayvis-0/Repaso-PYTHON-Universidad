#Ejemplo 10-1. Clase base abstracta MapBase

from collections.abc import MutableMapping

class MapBase(MutableMapping):
  """Nuestra propia clase base abstracta que incluye una clases _Item"""

  #----------------------------clase Item anidada-------------------------
  class _Item:
    """Componente ligero para almacenar un par clave-valor como item"""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __eq__(self, other):               
      return self._key == other._key   # compara items en base a su clave

    def __ne__(self, other):
      return not (self == other)       # negacion de __eq__

    def __lt__(self, other):               
      return self._key < other._key    # compara items en base a su clave
