# Una implementacion de la busqueda binaria

def busqueda_binaria(data, target, low, high):
    """Devuelve True si target es encontrado en la porcion indicada de la lista
    La busqueda solo considera la porcion desde data[low] a data[high]"""
    
    if low > high:
        
        return False
        
    else:
        mid = (low + high) // 2
        
        if target == data[mid]:
            
            return True
        
        elif target < data[mid]:
            # Recurriendo a la porcion izquierda
            
            return busqueda_binaria(data, target, low, mid-1)
        
        else:
            # recurriendo a la porcio derecha
            
            return busqueda_binaria(data, target, mid+1, high)
        
n = int(input('Cantidad de numeros: '))        
        
nume = sorted([int(input(f'Numero {i+1}: ')) for i in range(n)])

numero = int(input('Numero a buscar: ')) 

if busqueda_binaria(nume, numero, 0, n-1):
    print(f'El numero {numero} se encuentra en la lista de numeros')
    
else:
    print(f'El numero {numero} no se encuentra en la lista de numeros')