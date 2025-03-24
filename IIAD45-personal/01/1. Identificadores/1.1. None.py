# None

"""Crea una función que maneje una lista de empleados en una empresa. Cada empleado puede tener o no un mentor asignado. La 
función debe aceptar una lista de empleados y sus respectivos mentores (si los tienen) y devolver una lista donde los empleados
sin mentores asignados (None) reciban un mentor por defecto."""

import random as ran

def ment():
    
    nombres = ['Ana','Eliza','Maria','Flor','Juan','Roberto']
    nume = ran.randint(0,len(nombres)-1)
    
    return nombres[nume]

def empl_ment(list_empl_ment):
    
    nuevo_empl_ment = []
    
    for i, j in list_emple_ment:
        if j is None:
        
            nuevo_empl_ment.append((i, ment()))
        
        else:
            nuevo_empl_ment.append((i, j))
    
    return nuevo_empl_ment
            
list_emple_ment = [('Juan','Pepe'),('Pedro',None)]

print(empl_ment(list_emple_ment))