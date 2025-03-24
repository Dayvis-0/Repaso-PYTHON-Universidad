# Ejemplo 8-7. La clase LinkedBinaryTree 

from BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Representacion enlazada de una estructura de arbol binaria"""
    
    class _Node:
        __slots__='_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right 
            
    class Position(BinaryTree.Position):
        """Una abstraccion que representa la ubiacion de un elemento"""
        
        def __init__(self, container, node):
            """Constructo no sera invocado por el usuario"""
            self._container = container
            self._node = node
            
        def element(self):
            """Devuelve el elemento almacenado en esta posicion"""
            return self._node._element
        
        def __eq__(self, other):
            """Devuelve True si other representa la misma posicion"""
            return type(other) is type(self) and other._node is self._node
        
    def _validate(self, p):
        """Devolver el nodo asociado, si la posicion es valida"""
        if not isinstance(p, self.Position):
            raise TypeError('p debe ser de tipo Position')
        if p._container is not self:
            raise ValueError('p no pertenece a este contenedor')
        if p._node._parent is p._node:
            raise ValueError('p ya no es valido')
        return p._node 
    
    def _make_position(self, node):
        """Devuelve una instancia de Position para un nodo"""
        return self.Position(self, node) if node is not None else None 
    
    #------------- constructor del arbol binario -----------------
    def __init__(self):
        self._root = None
        self._size = 0
        
    #--------------------accesores publicos----------------------
    def __len__(self):
        """Devuelve el numero total de elementos en esta arbol"""
        return self._size 
    
    def root(self):
        """Devuelve la posicion de la raiz del arbol"""
        return self._make_position(self._root)
    
    def parent(self, p):
        """Devuelve la posicion del padre de p"""
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        """Devuelve la posicion del izquierdo de p"""
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        """Devuelve la posicion del derecho de p"""
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        """Devuelve el numero de hijos de la posicion p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        """Pone el elemento e en la raiz del arbol vacio y devuelve la posicion
        
        Origina ValueError si el arbol no esta vacio
        """
        if self._root is not None: raise ValueError('Raiz no existe')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        """Crea un nuevo hijo izquierdo para la posicion p
        
        Origina un ValueError si la posicion p es invalida
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError('Hijo izquierdo existe')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
    
    def _add_right(self, p, e):
        """Crea un nuevo hijo derecho para la posicion p
        
        Origina un ValueError si la posicion p es invalida
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError('Hijo derecho existe')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        """Reemplaza el elemento en la posicion p con e"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old 
    
    def _delete(self, p):
        """Borra en nodo en la posicion p y lo reemppaza con su hijo
        
        Devuelve el valor que ha sido almacenado en la posicion p
        Origina un ValueError si la posicion p es invalida o p tiene dos hijos
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p tiene dos hijo')
        child = node._left if node._left else node._right 
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child 
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child 
            else:
                parent._right = child 
        self._size -= 1 
        node._parent = node 
        return node._element 
    
    def _attach(self, p, t1, t2):
        """Adjunta los arboles t1 y t2 como los hijos izquierdo y derecho de p"""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('debe ser una hoja')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('los tipos de arbol deben coincidir')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node 
            node._left = t1._root
            t1._root = None 
            t1._size = 0 
        if not t2.is_empty():
            t2._root._parent = node 
            node._right = t2._root 
            t2._root = None 
            t2._size = 0 

lbt = LinkedBinaryTree()
lbt._add_root(6)
lbt._add_right(lbt.root(),8)
lbt._add_left(lbt.root(),4)
lbt._add_left(lbt.left(lbt.root()),3)
lbt._add_right(lbt.left(lbt.root()), 5)

print("    6    ")
print("   / \\ ")
print("  4   8 ")
print(" / \\ ")
print("3   5 ")


print("Preorden")
for n in lbt.preorder():
    print(n.element())

print("Postorden")
for n in lbt.postorder():
    print(n.element())

print("Primero en amplitud")
for n in lbt.breadhfirst():
    print(n.element())
    
print("Inorden")
for n in lbt.inorder():
    print(n.element())