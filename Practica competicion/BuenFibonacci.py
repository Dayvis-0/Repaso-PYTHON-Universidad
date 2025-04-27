"""def buen_fibonacci(n):
    if n <= 1 :
        return (n, 0)
    else: 
        (a, b) = buen_fibonacci(n-1)
        
        return (a+b, a)"""
        
"""
TODO Mostrar la secuencia fibonacci complejidad n 
 
def buen_fibo(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = buen_fibo(n-1)
        
        return (a+b, a)

nume = int(input("Numero: "))

list_fibo = [buen_fibo(j)[1] for j in range(1, nume+1)]    
    
print(list_fibo)
"""
        
        
# Complejidad n
def buen_fibonacci(n):
    
    if n == 1:
        most = [0]

        return most
    else:
        most = [0]
        n -= 1

        def helper(n):
            if n <= 1:
                most.append(n)
                return (n, 0)
            else:
                (a, b) = helper(n-1)
                most.append(a+b)    
                return (a+b, a) 

        helper(n)
            
        return most
    
nume = int(input("Numero: "))

print(buen_fibonacci(nume))