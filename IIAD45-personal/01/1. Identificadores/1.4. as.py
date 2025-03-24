"""Crear un sistema para gestionar una biblioteca utilizando POO. El sistema debe permitir la gestión de libros, miembros y préstamos de libros."""

class Libro:
    def __init__(self, titu, aut, isbn):
        self._titulo = titu
        self._autor = aut
        self._ISBN = isbn
        self._diponibilidad = True        
    
    def prestar(self):
        
        if not self._diponibilidad:
            raise Exception('El libro no esta disponibel')
    
    def devolver(self):
        
        self._diponibilidad = True
        
    def __str__(self):
        
        return f'{self._titulo} por {self._autor} (ISBN: {self._ISBN})'
    
class Miembro:
    def __init__(self, nom, id):
        self._nombre = nom
        self._ID_miembro = id
        self._libros_prestados = []
        
    def prestar_libros(self, libro):
        try:
            libro.prestar()
            self._libros_prestados.append(libro)
            
        except Exception as e:
            print(f'No se pude prestar el librp {e}')
            
    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            libro.devolver()
            self._libros_prestados.remove(libro)

class Biblioteca:
    def __init__(self, nomb):
        self._nombre = nomb
        self._libros =  []
        self._miembros =  []
        
    def agregar_libro(self, libro):
    
        self._libros.append(libro)
        
    def agregar_miembro(self, miembros):
        
        self._miembros.append(miembros)
        
    def prestar_libro(self, miembro, libro):
        if libro in self._libros and miembro in self._miembros:
            miembro.prestar_libros(libro)
            
    def devolver_libro(self, miembro, libro):
        if libro in miembro._libros_prestados:
            miembro.devolver_libro(libro)
            
libro1 = Libro('El Quijote','Miguel de Cervantes','12345678')
miembro1 = Miembro('Jose','001')
biblioteca = Biblioteca('Biblioteca Central')

biblioteca.agregar_libro(libro1)
biblioteca.agregar_miembro(miembro1)

biblioteca.prestar_libro(miembro1, libro1)
biblioteca.devolver_libro(miembro1, libro1)

print(libro1)