# Implementacion de la clase PositionList

from _DoubleLinkedBase import _DoubleLinkedBase

class PositionalList(_DoubleLinkedBase):
    """Un contenedor secuencial de elementos que permite acceso posicional"""
    
    #------------------- class Position anidada --------------------
    
    class Position:
        """Una abstraccion que representa la ubicacion de un elemento"""
        
        def __init__(self, container, node):
            """Constructor que no sera invocado por el usuario"""
            
            self._container = container
            self._node = node
            
        def element(self):
            """Develve el elemento almacenado en eesta posicon """
            
            return self._node._element
        
        def __eq__(self, other):
            """Devuelve True si una Position representa la misma ubicacion"""
            
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Devuelve True si otro no representa la misma ubicacion"""
            
            return not (self == other)
        
    #----------------------- metodo utilitario -------------------------
        
    def _validate(self, p):
        """Devuelve la posicion del nodo, u origina el error apropiado"""
        
        if not isinstance(p, self.Position):
            raise TypeError('P debe ser de tipo Position')
        if p._container is not self:
            raise ValueError('p no es parte de este contenedor')
        if p._node._next is None:
            raise ValueError('p ya no es valido')
        
        return p._node
    
    def _make_position(self, node):
        """Devolver instancia de Position para un nodo dado"""
        
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
        
    #-------------------- accesores --------------------------------
    
    def first(self):
        """Devuelve la primera posicion de la lista"""
        
        return self._make_position(self._header._next)
    
    def last(self):
        """Devolver la ultima posicion de la lista"""
        
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        """Devolver la posicion justo antes de la posicion p"""
        
        node = self._validate(p)
        
        return self._make_position(node._prev)
    
    def after(self, p):
        """devuelve la posicion justo despues de la posicion p"""
        
        node = self._validate(p)

        return self._make_position(node._next)
    
    def __iter__(self):
        """Genera una iteracion hacia adelante de los elementos de la lista"""
        
        cursor = self.first()
        
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
            
    #-------------------- modificadores --------------------------------
    def _insert_betweeen(self, e, predecesor, sucesor):
        """Agrega un elemento enter nodos existentes y devuelve Position"""

        node = super()._insert_betweeen(e, predecesor, sucesor)
        
        return self._make_position(node)
    
    def add_first(self, e):
        """Inserta el elemento e al frente de la lista y devuelve Position"""
        
        return self._insert_betweeen(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Inserta un elemento e al final de la lista y devuelve Position"""
        
        return self._insert_betweeen(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Inserta e en la lista antes de p y devuelve la nueva Position"""
        
        original = self._validate(p)
        
        return self._insert_betweeen(e, original._prev, original)
    
    def add_after(self, p, e):
        """Inserta e en la lista despues de p y devuelve la nueva Position"""
        
        original = self._validate(p)
        
        return self._insert_betweeen(e, original, original._next)
    
    def delete(self, p):
        """Remueve y devuelve el elemento een la posicion p"""
        
        original = self._validate(p)
        
        return self._delete_node(original)
    
    def replace(self, p, e):
        """Reemplaza y devuelve el element en la posicion p con e"""
        
        original = self._validate(p)
        old_value = original._element
        original._element = e
        
        return old_value
    
    def __str__(self):
        
        resu = ['[ '+str(e)+' ]' for e in self]
   
        return ' <-> '.join(resu)
    
posi = PositionalList()

posi.add_first(1)
posi.add_first(2)

print(posi)

p = posi.first()

print(p.element())