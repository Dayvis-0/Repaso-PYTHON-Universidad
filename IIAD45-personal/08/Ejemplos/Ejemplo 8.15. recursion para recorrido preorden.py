# recursion eficiente para imprimir la version identada del recorrido preorden

def preorder_ident(T, p, d):
    """Imprime la representacion preorden del subarbol de T con raiz en p y proofundidad d"""

    print(2*d*' '+str(p.element()))
    
    for c in T.childrin(p):
        
        preorder_ident(T, c, d+1)