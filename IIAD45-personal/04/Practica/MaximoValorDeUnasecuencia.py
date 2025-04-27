def maximo(lista):

    if len(lista) == 1:
        return lista[0]

    mitad = len(lista) // 2
    izqui = maximo(lista[:mitad])
    dere = maximo(lista[mitad:])

    return izqui if izqui > dere else dere

nume = [10,2,1000, 3,4]

print(maximo(nume))