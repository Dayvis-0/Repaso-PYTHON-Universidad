def parente_vali(expre):
    apertura = "([{"
    cierre = ")]}"
    S = []

    for c in expre:
        if c in apertura:
            S.append(c)
        elif c in cierre:
            if len(S) == 0:
                return False
            if cierre.index(c) != apertura.index(S.pop()):
                return False
    
    return len(S) == 0

nume = "{{[()]}}"

if parente_vali(nume):
    print("Si")
else:
    print("No")