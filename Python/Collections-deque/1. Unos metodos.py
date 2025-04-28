# Contenedor similar a una lista con appends y pops en ambos extremos  
from collections import deque

"""class collections.deque([iterable[, maxlen]])
Retorna unnuevo objeto deque inicializado de izquierda a derecha (usando append()) con 
datos de iterable. Si no especifica iterabl, el nuevo deque estara vacio"""

nume = deque([1,2,3])
# append(x) | Agrega x al lado derecho de deque 
nume.append(4)
# appendleft(x) | Agrega x al lado ixquierdo de deque
nume.appendleft(0)
# clear() | Retira todos los elementos del deque dejandolo con longitud 0
# nume.clear() 
# copy() | Crea una copia supperficial del deque 
uya = nume.copy()
print(f"Copia: {uya}")
# count(x) | Cuenta el numero de elementos del deque 
cuenta = nume.count(1)
# extend(iterable) | Extiende el lado derecho agregando elementos del argumento iterable
nume.extend([5,6,7])
# extendleft(iterable) | Extiende el lado izquierdo agregando elementos del argumento iterable
nume.extendleft([-1,-2])
# index(x[,start[,stop]]) | Retorna la posicion de x en el deque (en o despues del indice 
# start y antes del indice stop). Retorna la primera conincidencia o lanza valueError
reto = nume.index(1)
# insert(i, x) | Ingresa x en la posiciono i, Si el index es mas que maxlen, lanza un IndexError
nume.insert(0,-3)
# pop() | Elimina y retorn un elemento del lado derecho del deque. Si no hay elementos lanza IndexError
po1 = nume.pop()
# popleft() | Elimina y retorn un elemento del lado izquierdo del deque. Si no hay elementos lanza IndexError
po2 = nume.popleft()
# remove(value) | Elimina la primera aparicion de value. Si no encuentra, lanza un ValueError
nume.remove(1)
# reverse() | Invierte los elementos del deque en su lugar (in-place) y luego retorna none
nume.reverse()
# rotate(n=1) | Gira el deque n pasos a la derecha. Si n es negativo, lo gira hacia la derecha
nume.rotate(1)
nume.rotate(-1)
# maxlen | Tamaño maximo de un deque o None si no esta limitado
lon = nume.maxlen()

print(f"Original: {nume}\nCuenta los 1: {cuenta}\nPosicion de 1: {reto}\nMaxlen: {lon}")