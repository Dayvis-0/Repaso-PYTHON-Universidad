# Ejemplo 8-16. Recursion eficiente para imprimir una representacion indentada y etiquetada de un recorrido preorden

def preorder_label(T, p, d, path):
    """Imprime la representacion etiquetada del subarbol de T con raiz en p 
    y profundidad d"""
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[-1] += 1
    path.pop()