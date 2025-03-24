def suma_bina(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (start+stop)//2
        
        return suma_bina(S, start, mid) + suma_bina(S, mid, stop)
    
n = [1,2,3]

print(suma_bina(n,0,len(n)))