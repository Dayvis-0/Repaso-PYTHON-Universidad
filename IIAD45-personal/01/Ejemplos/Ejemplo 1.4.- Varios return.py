def contiene(lista,objetivo=0):
    for item in lista:
        if item == objetivo:
            
            return True
    return False

lista = [1,2,3,4,5,6,6]
busc = 6

print(contiene(lista,busc))