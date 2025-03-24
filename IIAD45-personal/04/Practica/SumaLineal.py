def suma_lineal(S, n):
    if n == 0:
        return 0
    else:
        return suma_lineal(S, n-1) + S[n-1]
    
n = [1,2,3]

print(suma_lineal(n, len(n)))