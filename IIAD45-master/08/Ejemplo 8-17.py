# Ejemplo 8-17. Funcion que imprime la cadena con representacion parentetica del arbol

def parenthesize(T, p):
    """Imprimir la representacion parentetica del subarbol de T con raiz en p"""
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '
            print(sep, end='')
            first_time = False
            parenthesize(T, c)
        print(')', end='')