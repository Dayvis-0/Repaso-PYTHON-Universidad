import time

# Proporciona soporte para medicion de tiempo 


""" time.time() - Devuelve el tiempo actual en segundos desde la epoca, que es un punto de referencia (generalmente el 1 de enero de 1970)""" 

star_time = time.time()

for i in range(100000):
    pass

end_time = time.time()

lapso = end_time - star_time


# time.sleep(x) - Pausa la ejecucion del programa durante un numero de segundos x

# time.localtime() - Devuelve la hora local del sistema -> sstruct_time - año, mes, dia, hora, minuto, segundo, dia_sema, dia_año, 
# horario_verano(0 no es verano, 1 esta en verano, -1 desconocido, no puede determinar si esta o no en horario verano)

local_time = time.localtime()
anio_local = local_time.tm_year
me_local = local_time.tm_mon

# time.gmtime() - Devuelve la hora en formato UTC (Coordinaded Universal Time)

utc_time = time.gmtime()
anio_utc = utc_time.tm_year
me_utc = utc_time.tm_mon

# time.strftime() - Se puede formatear la hora en una cadena con el formato que prefieras. Los codigos son:

""" %Y: Año con cuatro digitos - %m: Mes en dos digitos - %d: Dia del mes en dos digitos - %H: Hora en formato 24 horas - %M: Minutos - %S: Segundos"""

local_time1 = time.localtime()

format = time.strftime("%Y/%m/%d %H:%M:%S", local_time1)

# stime.strptime() - Convertir una cadena a tiempo - Los dos deben de tener el mismo formato

time_string = "2025-01-27 14:20:00"
time_obj = time.strptime(time_string,"%Y-%m-%d %H:%M:%S")

# Si se tiene un objeto struct_time, se puede convertir a un timestamp (numero de segundos desde la epoca) usando time.mktime()

time_obj1 = time.localtime()
timestamp = time.mktime(time_obj1)

# time.perf_conunter() - Para medir intervalos de tiempo con una mayor precision (microsegundos)

star = time.perf_counter()

for i in range(1000000):
    pass

end = time.perf_counter()

time_tard = end - star

# time.monotonic() - Devuelve el tiempo transcurrido desde un valor arbitrario, y es util para medir el tiempo de ejecucion en sistemas de reloj

star1 = time.monotonic()

for i in range(1000000):
    pass

end1 = time.monotonic()

time_tard1 = end1 - star1

print(time_tard1)