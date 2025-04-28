
def emparejar_htlml(raw):
    S = []
    
    j = raw.find("<")
    
    while j != -1:
        k = raw.find(">", j+1)

        if k == -1:
            return False
        
        eti = raw[j+1:k]
        
        if not eti.startswith("/"):
            S.append(eti)
        else:
            if len(S) == 0:
                return False

            if eti[1:] != S.pop():
                return False
            
        j = raw.find("<", k+1)
        
    return len(S) == 0
            
if emparejar_htlml("<h1>Hola</h1>"):
    print("Si")
else:
    print("No")