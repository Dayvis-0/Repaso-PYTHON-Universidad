# Ejemplo 8-5. Metodo Tree.height que computa la altura de arbol entero

def height(self, p = None):
    """Devuelve la altura del subarbol con raiz en la posicion p
    
    si p es None, devuelve la altura del arbol entero
    """
    if p is None:
        p = self.root()
    return self._height2(p)

