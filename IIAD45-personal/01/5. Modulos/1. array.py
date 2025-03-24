# Proporciona almacenamiento en array para tipos primitivos
import array as a  

arr = a.array('i',[1,2,3,4,])
""" Tipos
'b': entero con signo (1 byte) - 'B': entero sin signo (1 byte) - 'u': carácter Unicode (2 bytes) - 'h': entero con signo (2 bytes)
'H': entero sin signo (2 bytes) - 'i': entero con signo (4 bytes) - 'I': entero sin signo (4 bytes) - 'l': entero con signo (4 bytes)
'L': entero sin signo (4 bytes) - 'f': punto flotante (4 bytes) - 'd': punto flotante (8 bytes) 
Se puede agregar elementos con el appendend, interstar con inssert, eliminar con remove o pop, se puede utilizar el slicig.
Se puede calcular la lognitud con len, sumar con sum, el minimo con mi, el maximo con max, convertur a lista con list"""
#for num in arr:
#    print(num)

with open('array.bin','wb') as f:
    arr.tofile(f)# Escribir el contenido de un array directamente en un archivo binario
    
nuev_arr = a.array('i') # array.array(tipo, elemento)

with open('array.bin','rb') as f:
    nuev_arr.fromfile(f, len(arr))# Permite leer datos binarios desde un archivo y almacenarlos en un array
    
# Array mutidimensional

matriz = [
    a.array('i',[1,2,3]),
    a.array('i',[4,5,6]),
    a.array('i',[7,8,9])
]

#for i in matriz:
#    for j in i:
#        print(j,end=' ')
        
import timeit
"""timeit sirve para realizar benchmarks (pruebas de mantenimiento), para medir el tiempo de ejecucion de cualquier pequeño fragmento
de codigo"""

# Benchmarck arrays
array_time = timeit.timeit(stmt="for n in arr: pass", # stmt - statement(instruccion) - El codigo a medir
                           setup="import array; arr = array.array('i', range(1000))", # setup - codigo que se ejecuta antes de stmt para preparar el entorno 
                           number=1000 # cuantas veces se ejecuta stmt
)

# Benchmarck listas
list_time = timeit.timeit(stmt="for n in lst: pass", setup="lst = list(range(1000))", number=1000)

print(f"Tiempo con array: {array_time}")
print(f"Tiempo con lista: {list_time}")
