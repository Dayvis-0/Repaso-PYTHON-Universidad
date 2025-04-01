"""
Imagina que trabajas en el departamento de Recursos Humanos de una empresa y necesitas gestionar a los empleados de la 
organización. En la estructura de la empresa, los empleados se dividen en diferentes niveles, como empleados generales, 
supervisores y gerentes. Cada nivel tiene características específicas, pero todos comparten algunos atributos básicos.

#* 1 Clases Base
    Empleado → Representa a un empleado genérico de la empresa. Tiene los siguientes atributos:
        nombre: Nombre completo del empleado
        edad: Edad del empleado
        salario_base: Salario base mensual del empleado
    Departamento → Representa el departamento donde trabaja el empleado. Tiene los siguientes atributos:
        nombre_departamento: Nombre del departamento (Ej: Finanzas, Marketing, Tecnología)
        ubicacion: Ubicación del departamento dentro de la empresa (Ej: Piso 3, Edificio A)
#* 2 Clases Derivadas con Herencia Multinivel
    Supervisor → Hereda de Empleado y Departamento, y agrega los siguientes atributos adicionales:
        nivel_supervision: El nivel de supervisión del supervisor dentro de la jerarquía (Ej: Bajo, Medio, Alto)
        equipo_a_cargo: Una lista de empleados que supervisa el supervisor
    Gerente → Hereda de Supervisor, Empleado y Departamento, y agrega los siguientes atributos adicionales:
        presupuesto_asignado: Presupuesto que tiene el gerente para el departamento
        objetivos_estrategicos: Una lista de objetivos estratégicos del departamento bajo su gestión
#* 3 Requisitos del Programa
    1. Crear una colección de empleados, supervisores y gerentes, almacenando todos los objetos en una lista.
    2. Recorrer la colección con un ciclo (bucle) y para cada empleado hacer lo siguiente:
        Si es un Empleado general, imprimir su nombre y salario base.
        Si es un Supervisor, imprimir el nombre, el salario base y el equipo a su cargo. Además, evaluar el nivel_supervision. Si el nivel de 
            supervisión es Bajo, imprimir un mensaje: "Supervisor de bajo nivel, necesita formación".
        Si es un Gerente, imprimir el nombre, el presupuesto asignado y los objetivos estratégicos del departamento. Además, verificar si el 
            presupuesto asignado es inferior a 100,000, y si es así, imprimir el mensaje: "Presupuesto insuficiente para objetivos estratégicos".
    3. Usar condicionales para realizar las siguientes comprobaciones:
        Si un empleado tiene un salario base menor a 2,000, imprimir un mensaje que diga: "Salario bajo, revisar condiciones laborales".
        Si un Supervisor tiene más de 5 empleados a su cargo, imprimir un mensaje que diga: "Supervisor con demasiados empleados a cargo, revisión necesaria".
        Si un Gerente tiene más de 3 objetivos estratégicos, imprimir el mensaje: "Gerente con demasiados objetivos estratégicos, priorizar tareas".
    4. Contar cuántos empleados tienen un salario bajo, cuántos supervisores tienen demasiados empleados a su cargo, y cuántos gerentes tienen presupuesto insuficiente.
    5. Imprimir un resumen final con las estadísticas generales:
        Total de empleados con salario bajo
        Total de supervisores con demasiados empleados a cargo 
        Total de gerentes con presupuesto insuficiente
"""

import time

class Empleado:
    def __init__(self, nombre: str, edad: int, salario_base: float):
        self._nombre = nombre
        self._edad = edad
        self._salario_base = salario_base
      
class Departamento:
    def __init__(self, nombre_departamento: str, ubicacion: str):
        self._nombre_departamento = nombre_departamento
        self._ubicacion = ubicacion
        
class Supervisor(Empleado, Departamento):
    def __init__(self, nombre, edad, salario_base, nombre_departamento, ubicacion, nivel_supervision: int, equipo_a_cargo: int):
        Empleado.__init__(self,nombre, edad, salario_base)
        Departamento.__init__(self, nombre_departamento, ubicacion)
        self._nivel_supervision = nivel_supervision
        self._equipo_a_cargo = equipo_a_cargo
        
class Gerente(Supervisor, Empleado, Departamento):
    def __init__(self, nombre, edad, salario_base, nombre_departamento, ubicacion, nivel_supervision, equipo_a_cargo, presupuesto_asignado: float, objetivos_estrategicos: int):
        Supervisor.__init__(self, nombre, edad, salario_base, nombre_departamento, ubicacion, nivel_supervision, equipo_a_cargo)
        self._presupuesto_asignado = presupuesto_asignado
        self._objetivos_estrategicos = objetivos_estrategicos

empresa = [Empleado('Jose', 25, 1500), 
           Supervisor('Dayvis', 29, 3000, 'Ciencia', 'Cercad de ', 30, 4), 
           Gerente('Geron', 39, 5000, 'Ciecnia', 'Al frente del gerente', 40, 5, 200000, 6),
           Empleado('Carlos', 24, 1600), 
           Supervisor('Maria', 28, 2900, 'Ademicos', 'Cerca de Academicos', 20, 2), 
           Gerente('Yala', 35, 4500, 'Academicos', 'Cerca de Academicos', 45, 2, 90000, 2)]

cont_sala_bajo = 0
cont_super_emple_cargo = 0
cont_gere_presu_insu = 0

for perso in empresa:
    print('\n\tEmpleado')
    print(f'Nombre: {perso._nombre}\nEdad: {perso._edad}')
    
    if perso._salario_base < 1600:
        cont_sala_bajo += 1
            
    if isinstance(perso, Supervisor):        
        if perso._nivel_supervision < 25:
            print("Supervisor de bajo nivel, necesita formación")
            
        if perso._equipo_a_cargo > 3:
            cont_super_emple_cargo += 1
            
    if isinstance(perso, Gerente):        
        if perso._objetivos_estrategicos > 3:
            print("Gerente con demasiados objetivos estratégicos, priorizar tareas")
            
        if perso._presupuesto_asignado < 100000:
            cont_gere_presu_insu += 1

    time.sleep(2)

print(f"""\nTotal de empleados con salario bajo: {cont_sala_bajo}
Total de supervisores con demasiados empleados a cargo: {cont_super_emple_cargo} 
Total de gerentes con presupuesto insuficiente: {cont_gere_presu_insu}""")