# Algoritmodisjunto 2

def disjointed2(A, B, C):
    """Devuelve True si no hay un elemento en comun a todas las listas"""
    
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    
    return True

list1, list2, list3 = [1,2], [4,5], [7,8]

print(disjointed2(list1, list2, list3))