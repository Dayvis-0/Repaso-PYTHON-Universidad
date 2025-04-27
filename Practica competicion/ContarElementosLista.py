def cont_elem(n, cont=0):
    if n[cont] == n[-1]:
        return 1
    
    return 1 + cont_elem(n, cont+1)

nume = [1,2,3]

print(cont_elem(nume))