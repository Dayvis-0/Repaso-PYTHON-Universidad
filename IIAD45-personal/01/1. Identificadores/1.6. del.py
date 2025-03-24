"""Crea una clase llamada Producto con atributos como nombre, categoría y precio.
Implementa una clase llamada Inventario que gestione una lista de productos.
En la clase Inventario, añade métodos para:
Agregar productos al inventario.
Eliminar un producto específico del inventario utilizando el identificador del.
Mostrar todos los productos en el inventario.
Crea un objeto de la clase Inventario y añade varios productos.
Elimina uno de los productos utilizando el método correspondiente."""

class Producto:
    
    def __init__(self, nom, cate, pre):
        self._nombre = nom
        self._categoria = cate
        self._precio = pre
        
class Inventario:

    def __init__(self):
        self._lista_de_productos = []
        
    def agregar_producto(self, producto):
        
        self._lista_de_productos.append(producto)
        
    def eliminar_producto(self, producto_elim):
        
        for i, producto in enumerate(self._lista_de_productos):
            if producto._nombre == producto_elim:
                del self._lista_de_productos[i]
                break
        
    def mostrar(self):
        
        for producto in self._lista_de_productos:
            print(f'Nombre: {producto._nombre}, Categoria: {producto._categoria}')
            
producto1 = Producto('Arroz','Grano',2.50)
producto2 = Producto('Azucar','Dulce',3.00)

inven = Inventario()

inven.agregar_producto(producto1)
inven.agregar_producto(producto2)

inven.mostrar()

inven.eliminar_producto('Azucar')

print('\n')
inven.mostrar()