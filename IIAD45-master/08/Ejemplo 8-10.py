# Ejemplo 8-10. Una implementacion del metodo positions para la clase Tree

def positions(self):
    """Genera una iteracion de la posiciones del arbol"""
    return self.preorder()