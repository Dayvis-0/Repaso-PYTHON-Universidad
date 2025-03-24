# Ejemplo 4-3. Implementacion de la busqueda binaria

def busqueda_binaria(data, target, low, high):
    """Devuelve True si target es encontrado en la porcion indicada de la lista
    La busqueda solo considera la porcion desde data[low] a data[high]
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            #recurriendo a la porcion izquierda
            return busqueda_binaria(data, target, low, mid-1)
        else:
            #recurriendo a la porcion derecha
            return busqueda_binaria(data, target, mid+1, high)

nume = [1,2,3,4]
        
if busqueda_binaria(nume, 5, 0, len(nume)-1):
    print('si')
else:
    print('no')