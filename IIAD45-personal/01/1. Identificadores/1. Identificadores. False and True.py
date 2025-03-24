"""Identificadores. En pyhon son case-sensitive. Los identificadores pueden se una combinacion de letras, digitos y 
guiones bajos.No pueden empezar con un numero y hay 33 palabras especiales que no puedes usarse como identificadores:"""

# False/True

"""Verificación de Contraseñas Seguras: Diseña una función que valide contraseñas basadas en múltiples criterios (longitud 
mínima, inclusión de números y caracteres especiales, etc.). Usa False para indicar si alguna de las condiciones no se cumple."""

import re

def vali_cont(contra):
    
    if len(contra) < 5 or not re.search(r'[A-Z]',contra) or not re.search(r'[a-z]',contra) or not re.search(r'\d',contra) or not re.search(r'[@#$%&^+-=]', contra):
        return False
    
    return True
        
contra = input('Contrasenia: ')

if vali_cont(contra):
    print('La contraseña es valida')
else:
    print('la contraseña no es valida')
    