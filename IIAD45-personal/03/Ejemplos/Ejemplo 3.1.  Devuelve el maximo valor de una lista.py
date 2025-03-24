# Funcion que devuelve el maximo valor de una lista

def find_maximun(data):
    """Devulve el maximo valor de una lista"""
    
    bigger = data[0]
    
    for val in data:
        if val > bigger:
            bigger = val
            
    return bigger

numero = [1,2,2,3,999999,3,4,4,123123322222,4,4,45,4,10000]

print(f'El mas grande de los numeros es: {find_maximun(numero)}')