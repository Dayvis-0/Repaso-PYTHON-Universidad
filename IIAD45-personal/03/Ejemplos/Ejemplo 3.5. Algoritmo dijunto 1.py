# Algoritmo disjunto 1

def disjointed(A, B, C):
    """Devuelve Tre si no hay un elemento comun en todas las listas"""
    
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

list1, list2, list3 = [1,2], [4,5], [7,8]

print(disjointed(list1, list2, list3))