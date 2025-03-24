# Ejemplo 8-18. Calculo recursivo de espacio de un arbol. Asumimos que el metodo space() devuelve el espacio usado en esta posicion

def disk_space(T, p):
    """Devuelve el espacio total del subarbol de T con raiz en p"""
    subtotal = p.element().space()
    for c in T.children(p):
        subtotal += disk_space(T, c)
    return subtotal