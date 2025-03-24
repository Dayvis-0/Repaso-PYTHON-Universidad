#Ejemplo 10-2. Implementaciln de una UnsortesTableMap en base a MapBase

from MapBase import MapBase

class UnsortedTableMap(MapBase):
  """Map implementation using an unordered list."""
  """Implementacion de un map utilizando una lista no ordenada"""

  def __init__(self):
    """Creando un map vacio."""
    self._table = []                              # lista de items
  
  def __getitem__(self, k):
    """Devuelve el valor asociado a la clave k"""
    for item in self._table:
      if k == item._key:
        return item._value
    raise KeyError('Key Error: ' + repr(k))

  def __setitem__(self, k, v):
    """Asignando el valor v a la clave k, si ya hay k lo sobreescribe"""
    for item in self._table:
      if k == item._key:                          # Encuentra coincidnecia
        item._value = v                           # reasigna valor
        return                                    # y termina
    # no se encuentra coincidencia para k
    self._table.append(self._Item(k,v))

  def __delitem__(self, k):
    """Remueve el item asociado con la clave k"""
    for j in range(len(self._table)):
      if k == self._table[j]._key:                # Encuentra coincidencia
        self._table.pop(j)                        # remueve item
        return                                    # y termina
    raise KeyError('Key Error: ' + repr(k))

  def __len__(self):
    """Devuelve la cantidad de items en el map."""
    return len(self._table)

  def __iter__(self):                             
    """Generate iteration of the map's keys."""
    """Genera una iteracion al finla de las claves del map"""
    for item in self._table:
      yield item._key                             # yield la clave
