from collections import namedtuple as named, deque as deq, Counter as coun, OrderedDict as orde, defaultdict as defa, ChainMap as cha
""" collections - Es una biblioteca poderosa que proporciona varios tipos de datos adicionales sobre las  que vienen incorporadas
con python """

# namedtuple - Son una forma de crear tuplas con nombres asignados a cada posicion.

Punto = named('Punto',['x','y'])

p = Punto(1,2)

# deque - (doble cola) son las listas optimizadas para operaciones de insercion y eliminacion rapidas en ambos extremos     

D = deq([1,2,3,4])

D.append(5) #  insertar un elemento al final de la cola 
D.appendleft(0) # insertr un elemento al inicio de la cola

# Counter - son una subclase especial de diccionarios que se utilizan para contar elementos de una coleccion

cont = coun([1,2,1,3,1])

# OrderedDict - son diccionarios que mantienen el orden de los elementos conforme se agregan, a diferencia de los diccionarios estandar

od = orde()
od['uno'] = 1 
od['dos'] = 2
od['tres'] = 3
od['cero'] = 0

# defaultdict - son diccionarios que devuelven un valor por defecto si la clave no existe en lugar de levantar una excepsion

dd = defa(int)
dd['uno'] += 1
dd['dos']
dd['tres']

# ChainnMap - permite agrupar multiples diccionarios o mapeos y tratarlos como una unidad

a = {'uno':1,'dos':2}
b = {'tres':3,'cuatro':4}

cm = cha(a,b)

print(cm)