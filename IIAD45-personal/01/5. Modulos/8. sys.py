import sys
# Proporciona interaccion de un nivel adicional  con el interprete de Python 

# sys.argv - Permite acceder aa los argumentos de la linea de comandos 

num_arg = len(sys.argv)

"""print(num_arg)  se tiene que enviar argumentos al script python "d:/Universidad/IV CICLO/ALGORITMO Y ESTRUCTURA DE DATOS II/En casa/PYTHON/Repaso/IIAD45-personal/01/5. Modulos/8. sys.py" hola mundo
print(sys.argv) mostrar la lista de argumentos del script"""

# sys.version - Muestra la version de Python que estas utilizando

# sys.platform - Indica el sistema operativo en el que se esta ejecutando Python 

# sys.exit() - Termina la ejecucion del programa

#sys.exit(0) # 0 indica una salida exitosa

""" sys.stin, sys.stdout, sys.stderr - Estos objetos permiten manejar la entrada y la salida estandar directamente"""

# entrada = sys.stdin.readline().strip() # Leer entrada estandar

ori = sys.stdout
"""
with open("salida.txt","w") as archivo:
    sys.stdout = archivo
    print('Esste texto se guardara en el archivo')
    
sys.stdout = ori

print('Este texto se imprime en la consola')"""

#sys.stderr.write('Este es un mensaje de error')

# sys.getsizeof(objeto) - Devuelve el tamaño en bytes de un objeto

x = [1, 2, 3]
tam = sys.getsizeof(x)

# sys.modules - Es un diccionario que  contine todos los modulos importador en el programa

dicc = sys.modules

# sys.path - Lista de rutas donde Python busca los modulos para terminar 

ruta = sys.path

# sys.maxsize - El valor maximo que un entero puede tener en Python

max_ent = sys.maxsize

# sys.executable - Muestra la ruta del ejecutable de Python

ruta1 = sys.executable

# sys.getrefcount() - Controla el comportamiento del recolector de basura 

x = [1,2,3]
basu = sys.getrefcount(x) # Guarda cuantas referencias hay al objeto x 

 

print(basu)