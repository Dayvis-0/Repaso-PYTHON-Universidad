from collections.abc import MutableMapping

class MapBase(MutableMapping):
    """Nuestra propia clase base abstracta que incluye una class _Item"""

    #-------------------------- class Item anidada -----------------------
    class _Item:
        """Componenete ligero para almacenar un par clave-valor como item"""
        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value =value

        def __eq__(self, other):
            
            return self._key == other._key # Compara items en base a su clase

        def __ne__(self, other):
            
            return not (self == other) # Negacion de __eq__

        def __lt__(self, other):
            
            return self._key < other._key # Compara items en base a su clase