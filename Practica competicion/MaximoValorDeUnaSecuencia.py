def maximo(S):
    if len(S) == 1:
        return S[0]

    mid = len(S) // 2
    left = maximo(S[:mid])
    right = maximo(S[mid:])

    return max(left, right)

nume = [1,2,1]

print(f"El mayor es: {maximo(nume)}") 