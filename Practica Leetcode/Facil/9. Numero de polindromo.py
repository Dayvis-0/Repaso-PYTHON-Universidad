"""Dado un numero entero x, regreo truue si x es polindromo, y false de otra manera
#* Ejemplo 1:
    Entrada: x = 121
    Salida: cierto
    Explicacion: 121 se lee como 121 de ixquierda a derecha y de derecha a izquierda
#* Ejemplo 2:
    x = -121 | falso | -121 != 121-"""

class Solution:
    def isPolindrome(self, x: int) -> bool:
        x_srt = str(x) 
        resu = x_srt
        cont = -1

        for j in range(len(x_srt)//2):
            aux = x_srt[-1]
            resu[j] = x_srt[aux]
            