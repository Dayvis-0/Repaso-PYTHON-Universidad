# Enumerando y probando todas las posibles soluciones

def puzzle_solver(k, S, U):
    
    for e in U:
        
        Sn = S + [e]
        Un = list(U)
        Un.remove(e)

        if k == 1:
            print(Sn)
        else:
            puzzle_solver(k-1, Sn, Un)
    
puzzle_solver(2, [], [1,2,3,4])