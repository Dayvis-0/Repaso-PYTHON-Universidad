"""Ejercicio de Nivel Intermedio: Sistema de Clasificación de Calificaciones con POO

Escribe un programa en Python que clasifique las calificaciones de estudiantes utilizando POO 
y los identificadores if, else, y elif. El programa debería:

Crear una clase Estudiante con los siguientes atributos y métodos:

Atributos: nombre: para almacenar el nombre del estudiante. / calificacion: para almacenar la calificación del estudiante.

Métodos:

asignar_calificacion(calificacion): para asignar una calificación al estudiante.
clasificar_calificacion(): para clasificar la calificación del estudiante usando if, else, y elif, y mostrar la clasificación correspondiente.

La clasificación de las calificaciones debe seguir estas reglas:

>= 90: "Excelente"
>= 80 y < 90: "Bueno"
>= 70 y < 80: "Aceptable"
< 70: "Necesita mejorar"""

class Estudiante:
    
    def __init__(self, nom):
        self._nombre =  nom
        self._calificacion = 0
        self._corre = True
        
    def asignar_cali(self, cali):
        if 100>=cali>=0:
            self._calificacion = cali
        else:
            self._corre = False
            
    def clasi_cali(self):
        
        if self._corre:
            if self._calificacion >=90 :
                cali = 'Excelente '
                
            elif( 90 > self._calificacion >= 80):
                cali = 'Bueno'
                
            elif(80 > self._calificacion >= 70):
                cali = 'Aceptable'
                
            else:
                cali = 'Necesita mejorar'
                
            print(f'{self._nombre} tiene una clasificacion de su calificacion de {cali}')
            
        else:
            print('Calificacion incorrecta, debe de ser de (1-100)')
    
nom = input('Nombre: ')
cali = int(input('Calificacion: '))

es1 = Estudiante(nom)
es1.asignar_cali(cali)
es1.clasi_cali()