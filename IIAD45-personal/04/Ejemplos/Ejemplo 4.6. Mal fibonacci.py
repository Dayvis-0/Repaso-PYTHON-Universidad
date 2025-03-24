# Calculando el n numero Fibonacci usando recursividad 

def mal_fibonacci(n):
    
    if n <= 1:
        
        return n
    
    else:
        
        return mal_fibonacci(n-2) + mal_fibonacci(n-1)

print(mal_fibonacci(4))