# Simulacion de una Lista de Tareas

class Tarea:
    
    def __init__(self, nom, des, compl = False):
        self._nombre = nom
        self._descripcion = des
        self._completada = compl

    def __str__(self):
        
        return f'Tarea: {self._nombre}\nDescripcion: {self._descripcion}, \nCompletada?: {self._completada}\n'
        
                
class ListaDeTareas:
    
    def __init__(self):
        self._lista_tareas = []
        
    def agregar_tareas(self, tarea):
        
        self._lista_tareas.append(tarea)
        
    def marcar_como_completada(self, tarea):
        
        tarea._completada = True
        
    def mostrar(self):
        
        for tareas in self._lista_tareas:
            if tareas._completada:
                continue

            print(tareas)
            
ta1 = Tarea('Barrer','Barrer la casa, el baño, la cocina y el cuarto')
ta2 = Tarea('Cocinar','Cocinar lomo saltado')
ta3 = Tarea('Estudio','Practicar programacion en python')

lis1 = ListaDeTareas()

lis1.agregar_tareas(ta1)
lis1.agregar_tareas(ta2)
lis1.agregar_tareas(ta3)
lis1.mostrar()

print('A')
lis1.marcar_como_completada(ta1)
lis1.mostrar()