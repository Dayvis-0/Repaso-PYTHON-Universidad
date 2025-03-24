# Simulacion de una biblioteca

class Libro:
    def __init__(self, titu, aut, gene, dispo = True):
        self._titulo = titu
        self._autor = aut
        self._genero = gene
        self._diponible = dispo
        
    def __str__(self):
        
        return f'Nombre: {self._titulo} \nAutor: {self._autor} \nGenero: {self._genero} \n{self._}'