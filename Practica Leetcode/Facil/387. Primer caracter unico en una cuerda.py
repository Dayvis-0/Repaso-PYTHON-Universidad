"""Dada una cuerda s, encuentra el primer caracter no repetitivo en el y devolver su indice. Si no existe, regresa -1
Ejemplo 1:
s = "leetcode"
salida = 0 
Explicacion: El personaje 'l' en el indice 0 es el primer caracter que no ocurre en ningun otro indice"""

# Complejidad temporal O(n^2) y complejidad espacial O(1)
def prime_cara_no_re(text: str) -> int:
    
    for c in text:
        cont = text.count(c)
        if cont == 1:
            return text.index(c)
        
        if c == text[-1]:
            return -1
        
        cont = 0
    
# Complejidad temporal y espacial O(n)    
def prime_cara_no_re1(text: str) -> int:

    cont = {}

    for c in text:
        if c in cont:
            cont[c] += 1
        else:
            cont[c] = 1
            
    for i, c in enumerate(text):
        if cont[c] == 1:
            return i
    
    return -1
        
print(prime_cara_no_re("aabbal"))