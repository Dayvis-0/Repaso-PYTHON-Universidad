def power(x, n):
    if n == 0:
        return 1
    else:
        parcial = power(x, n//2)
        resu = parcial*parcial
        
        if n % 2 == 1:
            resu *= x
        
        return resu
    
print(power(2,10000))