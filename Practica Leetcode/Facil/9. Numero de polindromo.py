"""Dado un numero entero x, regreo truue si x es polindromo, y false de otra manera
#* Ejemplo 1:
    Entrada: x = 121
    Salida: cierto
    Explicacion: 121 se lee como 121 de ixquierda a derecha y de derecha a izquierda
#* Ejemplo 2:
    x = -121 | falso | -121 != 121-
    
* -2^31 <= x <= 2^31-1
Hacerlo sin convertirlo a cadena"""

class Solution:
    def isPolindrome(self, x: int) -> bool:

        mult = 1
        resu = 0
        divi = x % 10
                
        while divi > 0:
            resu = (divi)*mult + resu
            divi = divi % 10
            mult *= 10
            
print()