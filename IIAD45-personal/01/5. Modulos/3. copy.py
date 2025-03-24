import copy as co
# Define funciones generales para hacer copias de objetos
# Proporciona funciones para crear copias superficiales y profundas de objetos

# Asignacion de variables, en python cuando asignas una variable a otra, las dos variables referencian al mismo objeto 
a = [1,2,3]
b = a

a.append(4)

# copias superficial - copy.copy() - crea un nuevo objeto pero inserta referencias a los objetos contenidos en el original

list_orig = [1,2,3]
list_copy = co.copy(list_orig)

list_orig0 = [[1,2,3],[4,5,6]]
list_copy0 = co.copy(list_orig0)

list_orig.append(4) # solo se modifica la copia original 
list_copy.append(4) # solo se modifica la copia superficial 

list_copy[0] = 0 # solo se modifica la copia superficial

list_orig0[0][0] = 'modi1' # se modifican los dos 
#list_copy0[0][0] = 'modi' # se modifican los dos 

# copias profunda - copy.deepcopy() - crea un nuevo objeto y tambien crea copias de todos los objjetos contenidos en el originall

list_orig1 = [1,2,3]
list_copy1 = co.deepcopy(list_orig1)

list_orig2 = [[1,2,3],[4,5,6]]
list_copy2 = co.deepcopy(list_orig2)

list_orig1.append(4) # solo se modifica la copia original
list_copy1.append(4) # solo se modifica la copia profunda

#list_orig2[0][0] = 'modi' # solo se modifica la copia original 
list_copy2[0][0] = 'modi1' # solo se modifica la copia profunda


"""Se puede perzonalizar el comportamiento de copia. Las clases pueden definir sus propias formas de ser copiadas mediante los 
metodos especiales __copy()__ y __deepcopy__()"""

class MiClase:
    def __init__(self, valor):
        self._valor = valor
        
    def __copy__(self):
        # crear una nueva instancia y copiar el atributo
        nuev_copy = self.__class__(self._valor)
        nuev_copy.__dict__.update(self.__dict__)
        
        return nuev_copy
    
    def __deepcopy__(self, memo):
        # crea una nueva instancia y hacer una copia profunda del atributo
        nuev_copy = self.__class__(co.deepcopy(self._valor,memo))# co.deepcopy(objeto_a_copiar,diccionario)
        nuev_copy.__dict__.update(co.deepcopy(self.__dict__,memo))
        
        return nuev_copy

objeto_original0 = MiClase(10) 
copia0 = objeto_original0.__copy__()

objeto_original = MiClase([[1, 2], [3, 4]]) 
copia_profunda = co.deepcopy(objeto_original) 
copia_profunda._valor[0][0] = 'modificado' 

print("Valor del objeto original:", objeto_original._valor) 
print("Valor del objeto copiado:",copia_profunda._valor)