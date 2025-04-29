"""Dado un numero entero x, regreo truue si x es polindromo, y false de otra manera
#* Ejemplo 1:
    Entrada: x = 121
    Salida: cierto
    Explicacion: 121 se lee como 121 de ixquierda a derecha y de derecha a izquierda
#* Ejemplo 2:
    x = -121 | falso | -121 != 121-
    
* -2^31 <= x <= 2^31-1
Hacerlo sin convertirlo a cadena"""

class Solution(object):
    def isPolindrome(self, x: int) -> bool:
        if x < 0:
            return False

        resu = 0
        xcopy = x
                
        while x != 0:
            divi = x % 10
            resu = (resu)*10 + divi
            x //= 10
            
        if xcopy == resu:
            return True
        return False
    
so1 = Solution()

if so1.isPolindrome(121):
    print("Si")
else: 
    print("No")