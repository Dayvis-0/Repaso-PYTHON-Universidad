# Ejemplo 8-15. Recursion eficiente para imprimir la version indentada del recorrido preorden.

def preorder_indent(T, p, d):
    """Imprime la representacion preorden del subarbol de T con raiz en p 
    y profundidad d"""
    print(2*d*' '+str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d+1)