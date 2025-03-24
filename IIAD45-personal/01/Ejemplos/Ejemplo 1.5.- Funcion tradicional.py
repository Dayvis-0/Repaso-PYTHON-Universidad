def factores(n):
    resu = []
    for k in range(1,n+1):
        if n % k == 0:
            resu.append(k)
    
    return resu

print(factores(5))