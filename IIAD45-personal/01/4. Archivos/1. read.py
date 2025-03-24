"""fp.read - Devuelve el contenido de un archivo como string"""

# open(ruta, modo) - modo ->
# r.-Leer un archivo texto (debe de existir) - r b.-Leerun archivo en modo binario - w.-Escribir(sobreescribir) en un archivo de texto (si no existe se crea)
# wb.-Escribir en un archivo en modo binario - a.-agregar contenido a un archivo de texto (si no existe se crea) - ab.-Agregar contenido a un archivo en modo binario
# r+.-Leer y escribir (debe existir) - w+.- Leer y escribir(borra el existente) - a+.-Leer y agregar (si no existe se crea uno nuevo)
# rb+.-Leer y escribir en un archivo binario (debe existir) - wb+.-Leer y escribir en un archivo binario (borra el existente) 
# ab+.-Leer y agregar contenido en un archivo binario (si no hay, se crea)
arc1 = open('d:\\Universidad\\IV CICLO\\ALGORITMO Y ESTRUCTURA DE DATOS II\\En casa\\PYTHON\\Repaso\\IIAD45-personal\\01\\4. Archivos\\hola.txt','r+')

#abierto = arc1.read() 

"""fp.read(k) - Devuelve los isguientes k bytes de un archivo como string"""

#abierto = arc1.read(2)

""" fp.readlines() - Devuelve la linea actual de un archivo como una lista de strings"""

#abierto = arc1.readline()
#
#while abierto:
#    print(abierto)
#    abierto = arc1.readline()
    
""" fp.readlines() - Devuelve todas las lineas de un archivo como una lista de string"""

#abierto = arc1.readlines()

"""for line in fp - Iteral las lineas de un archivo"""

#for linea in arc1:
#
#    print(linea)

""" fp.seek(k) - Cambiar la actual posicion a la posicion k-esima del archivo"""

#arc1.seek(0) # Cursos en la posicion 0
#    nombre_.seek(offset,fromset) - (desplazamiento_en_bytes,donde_se_empieza_a_mover) para que funciione esto debe de ser asi rb para bytes mas
#arc1.seek(0,0) # Mover el cusros al principio del archivp
#arc1.seek(2,0) # Mover el cursos a 2 bytes desde el principio
#arc1.seek(0,1) # Mover el cursos 0 bytes desde la posicion actual(no cambia la posicion)
#arc1.seek(3,1) # Mover 3 bytes hacia adelante desde la posicion actual (donde sea que este el cursor)
#arc1.seek(0,2) # Mover al final del archivo y leer (devuelve vacion, ya que, esta al final)
#arc1.seek(-2,2) # Mover 2 bytes hacia atras desde el final y leer desde ahi 

""" fp.tell() - Devulve la posicion actual mediad como desplazamiento"""

#posi = arc1.tell() # Obtener la posicion actual del cursor 

""" fp.write(str) - Pone un string en la actual posicion en el archivo"""

#arc1.write('Bien')
#arc1.seek(0,0)

""" fp.wrietelines(seq) - Escribir cada uno de los strings de una secuencia dada en la posicion actual de un archivo"""

lineas = ['\nbien\n','ytu?']
arc1.seek(0,2)
arc1.writelines(lineas)
arc1.seek(0,0)
print(arc1.read())

arc1.close()