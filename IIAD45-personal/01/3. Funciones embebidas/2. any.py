# Devuelve True si bool(e) es True para al menos un elemento e
# Si un elemento de un iterable es verdadero -> True
# Si todos los elemento de un iterable son falsos -> False

# any(iterable)

nume1 = [1,2,3,4]
an1 = any(nume1)

nume2 = [0,0,0]
an2 = any(nume2)

nume3 = [-1,-5,2,5]
al3 = any([i < 0 for i in nume3])

print(an2)