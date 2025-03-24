import random

# Proporciona generacion de numeros aleatorios 
# Proporciona una serie de metodos para trabajar con numeros y secuencias aleatorias

# Numeros aleatorios simples 

ale = random.random() # Devuelve un número flotante aleatorio en el rango [0.0, 1.0)
alea_entre = random.randint(1, 2) # Devuelve un entero aleatorio N tal que a <= N <= b.
alea_entre_flo = random.uniform(1, 2) #  Devuelve un número flotante aleatorio tal que a <= N <= b

# Elegir elementos aleatoriamente

fruta = ['Manzana','Mango','Sandia','Ciruelo']
posi = [1,2,3,4]
ale_ele = random.choice(fruta) # Devuelve un elemento aleatorio de la secuencia seq.
alea_seq = random.choices(fruta, weights=None, k=3) # Devuelve una lista con k elementos seleccionados aleatoriamente de population, con o sin pesos.
alea_seq1 = random.choices(fruta, weights=posi,k=2)

# Barajar y reordenar secuencias

random.shuffle(fruta) # Baraja la secuencia 

fruta1 = ['Manzana','Mango','Sandia','Ciruelo']

list_sele = random.sample(fruta1,2) # Devuelve una lista de tamaño k con elementos unicos seleccionados de seq

# Distribuciones estadisticas

alea_gaus = random.gauss(0,1) # Devuelve un numero flotante basado en una distribucion gaussiana(normal) con media x y desciacion estandar y 
alea_exp = random.expovariate(1) # Devuelve un numero flotante basado en una distribucion exponencial con tasa x

#random.seed(42) # Inicializa el generador de numeros aleatorios -> inicializa el generador con la semilla 42, garantizando reproducibilidad

# Distribuciones especificas y funcionales 

"""random.betavariate(alpha,beta) - Generar un numero aleatorio que sigue a una distribucion beta con los parametros alpha y beta  

alpha (tambien llamado forma 1) controla la forma de la distribucion en el lado izquierdo (carca a 0)

beta (tambien llamado forma 2) controla la forma de la distribucion en el lado derecho (cerca a 1)

Distribucion beta.- es una distribucion de probabilidad continua en el intervalo [0,1] que se utiliza para modelar fenomenos
como probabilidades, tasas de conversion, o proporciones. La distribucion beta es controlada por dos parametros alpha y beta.
Estos parametros determinar la forma de la distribbucion.

Si alpha > beta, la distribucion estara sesgada hacia 1 (valores cercanos a 1 seran mas probables)
Si alpha < beta, la distribucion estara sesgada hacia 0 (valores cercanos a 0 seran mas probables)
Si alpha = beta, la distribucion sera simetrica en torno a 0.5
Si ambos alpha y beta son grandes, la distribucion sera mas concentrada cerca de 0.5
Si ambos alpha y beta son pequeños, la distribucion tendra mas probabilidad de generar valores cercanos a 0 o a 1"""
num_bet = random.betavariate(2,5) 

"""random.gammavariate(alpha,beta) - Generar un numero aleatorio que sigue una distribucion Gamma con los parametros alpha(forma) y beta(escala).

Dsitricuion de Gamma.- Es una distribucion continua muy utilizada en estadistica y modelado, especialmente cuando se trata
de tiempos de espera, procesos de Poisson, y fenomenos donde los valores son siempre positivos.

alpha(o k, tambien llamado 'parametro de forma'): Determina la forma de la distribucion. Si alpha es un numero entero, la
distribucion puede representar una suma de alpha variables aleatorias exponenciales

beta(o 0, tambien llamado (parametro de escala)): Escala la distribucion y controla la dispersion de los valores generados. Un valor mas pequeño que 
beta resulta en una disstribucion mas concentrada, mientras que un valor mas grande de beta hace que los valores se distribuyan mas ampliamente

Si alpha es pequeño (como 1), la distribucion sera mas sesgada hacia 0
Si alpha es grande, la distribucion se vuelve mas suave y similar una distribucion normal"""

nume_gam = random.gammavariate(2,2)

"""random.weibullvariable(alpha,beta) - Devuelve un numero basado en la distribucion de Weibull

Distribucion de Weibull.- Es una distribucion de probabilidad continua qque se usa principalmente para modelar tiempos de vida, fallos, o procesos
que dependen del tiempo.. Es especialmente util en analisis de supervivencia, y en el estudio de tiempos de espera o vida util de los productos

alpha (parametro de forma).- Controla la forma de la distribucion

beta (parametro de escala).- Controla la escala de la disribucion 

alpha -> Si es = 1, la distribucion se convierte en una distribucion exponencial - Si es < 1, la distribucion tiene una forma sesgada hacia la 
izquierda, indicando que los valores mas pequeños son mas probables - Si es > 1, la distribucion tiene una forma sesgada hacia la derecha, lo
que significa que los valores mas grandes son mas probables """

ale_wei = random.weibullvariate(1.5,1.5)

print(ale_wei)