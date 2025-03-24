# Calculando potencia usando cuadrados repetidos 

def power(x, n):
    """Calcula el valor de x**n"""
    
    if n == 0:
        
        return 1
    
    else:
        parcial = power(x, n // 2)
        result = parcial * parcial
        
        if n % 2 == 1:
            result *= x
        
        return result
        
print(power(2,3))