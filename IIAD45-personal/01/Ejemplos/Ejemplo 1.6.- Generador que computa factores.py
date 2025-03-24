def factores(n):
    result = []
    
    for i in range(1,n+1):
        if n % i == 0:
            result.append(i)    
            yield i

lista_gene = list(factores(4))
            
for i in factores(4):
    
    print(i)