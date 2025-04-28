"""Metodo index: complejidad temporal O(n) y espacial O(1)
Complejidad: temporal O(n) espacial O(n)"""
    
def deli_verda(text):
    aper = "({["
    cier = ")}]"

    stack = []

    for te in text:
        if te in aper:
            stack.append(te)
        elif te in cier:
            if len(stack) == 0:
                return False
            if cier.index(te) != aper.index(stack.pop()):
                return False
        
    return len(stack) == 0

if deli_verda("(12{d})"):
    print("si")
else:
    print("no")