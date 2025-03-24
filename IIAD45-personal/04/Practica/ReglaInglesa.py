def dibu_line(long, eti=''):
    
    linea = '-'*long
    
    if eti:
        linea += ' '+eti
        
    print(linea)
    
def dibu_inte(marca):
    
    if marca > 0:
        dibu_inte(marca - 1)
        dibu_line(marca)
        dibu_inte(marca - 1)

def dibu_regla(pulg, mayor):
    
    dibu_line(mayor, '0')
    
    for j in range(1, 1 + pulg):
        dibu_inte(mayor-1)
        dibu_line(mayor, str(j))
    
dibu_regla(2,3)