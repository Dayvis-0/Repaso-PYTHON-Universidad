# Calculando la potencias usando una recursividad lineal

def power(x, n):
    """Calcula el valor de x^n"""
    
    if n == 0:
        
        return 1
    
    else: 
        
        return x*power(x, n-1)
    

print(power(2,3))