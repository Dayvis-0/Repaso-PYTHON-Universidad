# Implementacion de una UnsortedTableMap en base a Mapbase

from MapBase import MapBase

class UnsortedTableMap(MapBase):
    """Implementacion de un map utilizando una lista no ordenada"""

    def __init__(self):
        """Creando un map vacio"""

        self._table = []                            # Lista de items

    def __getitem__(self, key):
        """Devuelve el valor asociado a la clave k"""

        for item in self._table:
            if key == item._key:
                return item._value

        raise KeyError('Key Error: ' + repr(key))

    def __setitem__(self, key, value):
        """Asignando el valor value a la clave key, si hay un key lo sobreescribe"""

        for item in self._table:                    # Encuentra coincidencia
            
            if key == item._key:                    # reasigna valor
                item._value = value                 
                
                return                                  # y termina
        
        # No se encuentra coincidencia para key
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        """Remove el item asociado con la clave key"""

        for j in range(len(self._table)):           # Encuentra coincidencia
            if key == self._table[j]._key:            # remueve item
                self._table.pop(j)

                return                              # y termina

        raise KeyError('Key Error: ' + repr(key))
    
    def __len__(self):
        """Devuelve la cantidad de items en el map"""

        return len(self._table)

    def __iter__(self):
        """Genera una iteracion al final de las claves del map"""

        for item in self._table:
            
            yield item._key                     # yield la clave