# Programa que calcule el MCM (Minimo Comun Miltiplo)

def MCDDeDosNumeros(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b

    return a

# Se sabe que el MCM de dos numeros es igual a: (a*b)/ mcd
def MCMDeDosNumeros(a: int, b:int) -> int:
    return (a*b) / MCDDeDosNumeros(a, b)

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

print(f"El MCM de los dos numeros es: {MCMDeDosNumeros(n1, n2)}")