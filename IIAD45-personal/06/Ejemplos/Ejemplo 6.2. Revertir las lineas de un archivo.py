from ArrayStack import ArrayStack

def revertir_archivo(archivo):
    """Sobreescribe el archivo con su contenido revertido"""
    
    S = ArrayStack()
    
    with open(archivo, 'r') as original:
        for linea in original:
            S.push(linea.rstrip('\n'))
        
    with open(archivo, 'w') as salida:
    
        while not S.is_empty():
            salida.write(S.pop() + '\n')  
    
revertir_archivo(r"d:\Universidad\IV CICLO\ALGORITMO Y ESTRUCTURA DE DATOS II\En casa\PYTHON\Repaso\IIAD45-personal\06\Ejemplos\aaa.txt")