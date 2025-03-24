def num_pares(n, s=0):
    if n > 0:
        print(s) 
        num_pares(n-1, s+2)
        
num_pares(5)