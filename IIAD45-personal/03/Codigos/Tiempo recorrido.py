from time import time

start_time = time()

for i in range(1000000):
    pass

end_time = time()

print(f'Tiempo recorrido en segundo al relaizar el algoritmo: {end_time-start_time}')
