"""Desarrollar un sistema para gestionar el inventario de una tienda utilizando POO. El sistema debe permitir la gestión de 
productos, realizar ventas y controlar el stock."""

class Producto:
    def __init__(self, nom, codi, pre, canti):
        self._nombre = nom
        self._codigo = codi
        self._precio = pre
        self._cantidad_stock = canti
        
    def reducir_stock(self, cantidad):
        
        assert cantidad <= self._cantidad_stock
        
        if self._cantidad_stock == 0:
                
            return 'Ya no hay mas stock'

        self._cantidad_stock -= cantidad

    def aumentar_stock(self, aumentar):
        
        self._cantidad_stock += aumentar
        
    def __str__(self):
        
        return f'{self._nombre} (Codigo: {self._codigo}, Precio: {self._precio})'

class Tienda:
    
    def __init__(self, nom):
        self._nombre = nom
        self._lista_productos = []
        
    def agregar_producto(self, producto):
        
        self._lista_productos.append(producto)
        
    def realizar_ventas(self, codigo_producto, cantidad):
        for producto in self._lista_productos:
            if codigo_producto == producto._codigo:
                producto.reducir_stock(cantidad)
                
                print(f'\nVenta realizada: {producto} -- Cantidad vendida {cantidad}')
                return 
        
        print('Producto no encontrado')
        
    def mostrar_inventario(self):
        for producto in self._lista_productos:
            print(producto)
        
producto1 = Producto("Laptop", "001", 1500.0, 10)
producto2 = Producto("Mouse", "002", 25.0, 50)

tienda = Tienda("Tienda Tech")
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

tienda.mostrar_inventario()

tienda.realizar_ventas('001',1)
tienda.realizar_ventas('002',1)