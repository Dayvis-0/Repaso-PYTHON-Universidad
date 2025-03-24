# Tablero de ajedrez con listas

tablero = [
    ['t','c','a','R','r','a','c','t'],
    ['p','p','p','p','p','p','p','p'],
    ['_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_'],
    ['p','p','p','p','p','p','p','p'],
    ['t','c','a','R','r','a','c','t'],
]

muestra = [print(i) for i in tablero]

# Mover un peon 
tablero[4][0] = 'p'
tablero[6][0] = '_'

print('\n\tMover un peon\n')
muestra = [print(i) for i in tablero]