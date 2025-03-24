def contar(lista, buscar):
    n = 0
    for item in lista:
        
        if item == buscar:
            n += 1
            
    return n

lista = [1,2,3,5,2,5]
busc = 5

print(contar(lista,busc))