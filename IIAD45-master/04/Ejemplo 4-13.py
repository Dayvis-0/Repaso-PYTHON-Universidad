# Ejemplo 4-13. Enumerando y probando todas las posibles soluciones

def puzzle_solver(k, S, U):
    for e in U:
        Sn = S + [e]
        Un = list(U)
        Un.remove(e)
        if k==1:
            print(Sn)
        else:
            # if not encontrado:
            puzzle_solver(k-1, Sn, Un)
        Sn.remove(e)
        Un = [e] + Un

puzzle_solver(2,[],[0,1,9])