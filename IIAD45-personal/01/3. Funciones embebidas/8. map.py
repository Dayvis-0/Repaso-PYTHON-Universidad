# Devuelve un iterador del resultado de la funcion

# map(func,iter1,iter2)

def suma_uno(x):
    
    return x + 1

li1 = [1,2,3]
resu = map(suma_uno, li1)

print(list(resu))