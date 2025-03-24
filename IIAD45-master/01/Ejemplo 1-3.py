def contar(data, target):
    n = 0
    for item in data:

        if item == target:
            n += 1
    return n

lista = [1, 3, 4, 5, 3]
buscado = 3

print(contar(lista, buscado))
