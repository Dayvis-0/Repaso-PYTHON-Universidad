import math

raiz = math.sqrt(16) 
poten = math.pow(2, 3) 
absolu = math.fabs(-5) # Valor absoluto de un numero
redo1 = math.ceil(4.2)  # Redondea hacia arriba, al entero mas cercano -> 5 
redo2 = math.floor(4.8)  # Redondea hacia abajo, al entero mas cercano -> 4
signo = math.copysign(2, -3) # Devuelve x con el signo de y  

cons = math.pi # Constante pi 
cons1 = math.e  # Constante e (base del logaritmo natural) euler

seno = math.sin(math.pi/2)  # marh.sin(numero en radianes)
cose = math.cos(math.pi) 
tang = math.tan(math.pi/4)  
aseno = math.asin(.1)

radi_gra = math.degrees(math.pi/2) # Convierte x de radianes a grados   
gra_rad = math.radians(180) # cConvierte x grados a radianes

loga = math.log(8, 2) # Logaritmo de x en base a   
loga_10 = math.log10(100) # Logaritmo base 10 de x  
expo = math.exp(2) # Calcula el valor de e^x  
expo_1 = math.expm1(1) # Calcula e^x - 1 de manera precisa para x pequeño

suma_ite = math.fsum([0.1, 0.2, 0.3, 0.4]) # Suma de un iterable, como una lista, precisa para grandes sumatorias
pro_ite = math.prod([1, 2, 3, 4]) # Calcula el producto de los elementos en un iterable 

es_inf = math.isinf(float('inf')) # Verifica si x es infinito 
es_nan = math.isnan(float('nan')) # Verifica si x es NaN (Not a Number)  
es_cerc = math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9) # Compara dos valores para determinar si estan cercanos entre si segun las tolerancias especificas  

fun_err = math.erf(1) # Devuelve la funcion de error de x 
fun_err_com = math.erfc(1) # Devuelve la funcion de error complememntaria de x 
fun_gamm = math.gamma(2.5) # Devuelve la funcion gamma de x 
fun_gamm_l = math.lgamma(2.5) # Devuelve el logaritmo natural de la funcion gamma
