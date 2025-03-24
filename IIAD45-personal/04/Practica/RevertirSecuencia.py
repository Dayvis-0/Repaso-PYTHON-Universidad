def revertir(S, start, stop):
    
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        revertir(S, start+1, stop-1)
    
    return S

nume = [1,2,3,4]

print(revertir(nume, 0, len(nume)))