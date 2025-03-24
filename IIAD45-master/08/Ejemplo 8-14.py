# Ejemplo 8-14. Definiendo el metodo BinaryTree.position de modo que todas las posiciones usaran en el recorrido inorden

def positions(self):
    """Genera una iteracion de las tres posiciones"""
    return self.inorder()
    
