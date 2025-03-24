# Un sript en python tipíco 

print('Hola mundo')
print('Ingrese sus notas, una por linea')
print('Ingrese una linea en blanco para indicar el final')

num_nota = 0
total_notas = 0
termi = 0

while not termi:
    
    nota = input()
    if nota == '':
        termi = True
    else:
        num_nota += 1
        total_notas = float(nota)
        
    if num_nota > 0:
        print('Tu promedio es {0:.3}'.format(total_notas/num_nota))