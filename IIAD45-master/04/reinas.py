def ocupadoN(i, j, tablero):
    if i < 0:
        return False
    return tablero[i][j] or ocupadoN(i-1, j, tablero)

def ocupadoS(i, j, tablero):
    if i > len(tablero)-1:
        return False
    return tablero[i][j] or ocupadoS(i+1, j, tablero)

def ocupadoE(i, j, tablero):
    if j > len(tablero[0])-1:
        return False
    return tablero[i][j] or ocupadoE(i, j+1, tablero)

def ocupadoO(i, j, tablero):
    if j < 0:
        return False
    return tablero[i][j] or ocupadoO(i, j-1, tablero)

def ocupadoNE(i, j, tablero):
    if i < 0 or j > len(tablero[0])-1:
        return False
    return tablero[i][j] or ocupadoNE(i-1, j+1, tablero)

def ocupadoSE(i, j, tablero):
    if i > len(tablero)-1 or j > len(tablero[0])-1:
        return False
    return tablero[i][j] or ocupadoSE(i+1, j+1, tablero)

def ocupadoNO(i, j, tablero):
    if i < 0 or j < 0:
        return False
    return tablero[i][j] or ocupadoNO(i-1, j-1, tablero)

def ocupadoSO(i, j, tablero):
    if i > len(tablero)-1 or j < 0:
        return False
    return tablero[i][j] or ocupadoSO(i+1, j-1, tablero)

ancho = 8
alto = 8
tablero = [ [0 for n in range(ancho)] for m in range(alto)]

print(tablero)