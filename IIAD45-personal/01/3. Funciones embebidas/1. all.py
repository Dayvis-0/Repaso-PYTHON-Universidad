# Devuelve True si bool(e) es True para cada elemento de e 
# Si todos los elementos de un iterable son verdaderos -> True
# Si un elemento del iterable es falso -> Fale

# all(iterable)

nume = [1,2,3,4]
al1 = all(nume)

nume1 = [0,1,2,3]
al2 = all(nume1)

nume3 = [1,2,3,4]
al3 = all([i > 0 for i in nume3])

print(al3)