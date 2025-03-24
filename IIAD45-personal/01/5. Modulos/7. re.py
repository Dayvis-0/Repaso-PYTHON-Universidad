import re

# Proporciona soporte para expresiones regulares

"""Se utiliza para trabajar con expresiones regulares(regex), Las expresiones regulares son secuencias de caracteres que forman un patro
de busqueda, y se utilizan para realizar busquedas y manipulaciones de texto de manera eficiente """

# re.match(pattern,string) - Busca si el patron coincide al inicio de la cadena. Si hay coincidencia, devuelve un match object, sino None

resu = re.match(r'Hola','Hola mundo') 

# re.search(pattern,string) - Busca el patron en toda la cadena y devuelve el primer mathc que encuentra (si lo encuentra). Si no encuentra devuelve none

resu1 = re.search(r'mundo','Hola mundo')

# re.findall(pattern,string) - Devuelve una lista con todas las coincidencias no solapadas del patron en la cadena 

tex = "Hola, soy Dayvis , Hola, soy Ana, Hola, soy Maria"
resu2 = re.findall(r'Hola',tex)

# re.finditer(pattern,string) - similar a findall, pero devuelve un iterador de objetos match en lugar de una lista esto permite obtener
# mas informacion de sobre cada coincidencia (como la posicion de la coincidencia)

tex1 = "La fecha de ayer fue 22/01/2025 y la de hoy es 23/01/2025"
resu3 = re.finditer(r'\d',tex1)

"""for match in resu3:
    print(f'Encontrado {match.group()} en la posicion {match.start()} y termina en {match.end()}')"""
    
# re.sub(pattern, repl, string) - Reemplaza las coincidencias del patron con una nueva cadena 

tex2 = "a,b,c,d,f"
tex_modi = re.sub(r'f','e',tex2)

# re.split(pattern, string) - Divide la cadena en una lista de subcadenas, usando el patron como delimitador 

tex3 = '1,2,3' 
part = re.split(r',',tex3)


print(part)