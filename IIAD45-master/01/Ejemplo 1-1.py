print("bienvenido a la calculadora")
print('ingrese todas sus notas, una por linea')
print('ingrese una linea en blanco para indicar el final.')

num_notas = 0
total_notas = 0
terminado = 0 #cambiara a 1 si se ha terminado

while not terminado:
  nota = input()
  if nota == '':
     terminado = True
  else:
     num_notas += 1
     total_notas += float(nota)
if num_notas > 0:
  print("Tu promedio es {0:.3}".format(total_notas/num_notas))
