#Aplicacion de seguimiento de tareas

class Tarea:
    def __init__(self, nom, com = False):
        self._nombre = nom
        self._completada = com
        
    def completada(self):
        
        self._completada  = True
        
        return (f'Tarea {self._nombre} completada')
        
class GestorTareas:
    def __init__(self):
        self._tareas = []
        
    def agregar_tarea(self, nombre):
        
        self._tareas.append(nombre)
        
    def completar_tarea(self, nombre):
        
        def contador_completadas():
            cont = 0
            for tarea in self._tareas:
                if tarea._completada:
                    cont += 1
                    
                return cont
            
        for tareas in self._tareas:
            
            if tareas._nombre == nombre:
                tareas.completar()
                break
        else:
            return (f'Tarea {nombre} no encontrada')
        
        completadas = contador_completadas()
        return (f'Tareas copletadas: {completadas}')
    
    def __str__(self):
        
        return  
    
ta1 = Tarea('Correr')
ta1 = Tarea('Barrer')
ta1 = Tarea('Cantar')

ges = GestorTareas()