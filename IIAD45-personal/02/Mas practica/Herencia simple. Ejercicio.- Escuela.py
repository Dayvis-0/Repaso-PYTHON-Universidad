"""
En una escuela, se tiene una clase base llamada Persona, que tiene atributos como el nombre, edad y género. De esta clase base, se derivan dos clases hijas:
    Estudiante: Representa a un estudiante, y tiene un atributo adicional llamado nota_final.
    Profesor: Representa a un profesor, y tiene un atributo adicional llamado asignatura que indica la materia que enseña.
#* Requerimientos:
    1. Crea una lista llamada personas que contenga varios objetos tanto de tipo Estudiante como de tipo Profesor.
    2. Recorre la lista de personas utilizando un bucle y, dependiendo del tipo de la persona, muestra su nombre y una información relevante:
        Si es un Estudiante, muestra su nombre y su nota final.
        Si es un Profesor, muestra su nombre y la asignatura que imparte.
    3. Además, debes verificar en cada iteración si la persona es un Estudiante con una nota final superior a 6. Si es así, imprime un mensaje que 
        diga "Estudiante aprobado". Si no, imprime "Estudiante reprobado".
    4. Si la persona es un Profesor, verifica si la asignatura que enseña es "Matemáticas". Si es así, imprime un mensaje que diga "Profesor de 
        Matemáticas". Si no, imprime el mensaje "Profesor de otra asignatura".
    5. Después de recorrer todas las personas en la lista, cuenta cuántos estudiantes aprobaron (aquellos con una nota final superior a 6) y cuántos
        profesores enseñan Matemáticas.
#* Reglas:
    Utiliza herencia simple para crear las clases Estudiante y Profesor que hereden de la clase base Persona.
    Utiliza condicionales para verificar las condiciones de aprobación de los estudiantes y la asignatura de los profesores.
    Utiliza un bucle para recorrer la lista de personas.
    Utiliza colecciones para almacenar las instancias de las personas.
#* Instrucciones:
    Define la clase Persona con los atributos básicos (nombre, edad, género).
    Define la clase Estudiante que herede de Persona y añada el atributo nota_final.
    Define la clase Profesor que herede de Persona y añada el atributo asignatura.
    Crea una lista personas que contenga varios estudiantes y profesores.
    Recorre la lista y realiza las verificaciones y el conteo de aprobados y profesores de Matemáticas.
"""

import time

class Persona:
    def __init__(self, nombre: str, edad: int, genero: str):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        
class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, genero: str, nota_final: int):
        super().__init__(nombre, edad, genero)
        self._nota_final = nota_final
        
class Profesor(Persona):
    def __init__(self, nombre: str, edad: int, genero: str, asignatura: str):
        super().__init__(nombre, edad, genero)
        self._asignatura = asignatura

personas = [Estudiante('Dayvis', 19, 'Masculino', 20), Profesor('Brayan', 30, 'Masculino', 'Matematicas'), 
            Estudiante('Maria', 20, 'Femenino', 18), Profesor('Rosa', 28, 'Femenino', 'Comunicacion'),
            Estudiante('Jose', 18, 'Masculino', 16), Profesor('James', 30, 'Masculino', 'Matematicas')]

cont_apro = 0
cont_pro_mate = 0

for persona in personas:
    print('\n')
    if isinstance(persona, Estudiante):
        print('\tEstudiante')
        print(f'Nombre: {persona._nombre}\nNota final: {persona._nota_final}')
        
        if persona._nota_final > 10.5:
            print('Estudiante aprobado')
            cont_apro += 1
        else:
            print('Estudiante reprobado')
    else:
        print('\tProfesor')
        print(f'Nombre: {persona._nombre}\nAsignatura que imparte: {persona._asignatura}')
        
        if persona._asignatura == 'Matematicas':
            print('Profesor de Matematicas')
            cont_pro_mate += 1
        else:
            print('Profesor de otra asignatura')
            
    time.sleep(2)
            
print(f'\nHay {cont_apro} aprobados')
print(f'Hay {cont_pro_mate} profesores de Matematicas')