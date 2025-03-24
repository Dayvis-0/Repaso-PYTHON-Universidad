"""
Cmplejidad temporal O(n)
Complejidad espacial O(n)

def buen_fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = buen_fibonacci(n-1)

        return (a+b, a)"""

# Cmplejidad temporal O(logn)
# Complejidad espacial O(logn)
        
def matri(A, B):
    """Multiplica dos matrices 2x2"""
    
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]], 
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]] 
    
def matri_exp(F, n):
    """Eleva la matriz F a la ppotencia n usando exponenciacion rapida"""

    if n == 0:
        return [[1,0],
                [0, 1]]

    if n == 1:
        return F
    
    if n % 2 == 0:
        half_power = matri_exp(F, n//2)

        return matri(half_power, half_power)
    else:
        
        return matri(F, matri_exp(F, n - 1))

def fibo(n):    

    if n == 0:
        return 0

    base_matri = [[1,1],
                  [1,0]]
    resu = matri_exp(base_matri, n - 1)
    
    return resu[0][0]

print(fibo(4))