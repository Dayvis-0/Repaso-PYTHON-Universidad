"""
Una cadena de restaurantes quiere desarrollar un sistema para gestionar los pedidos de los clientes de manera eficiente, asegurando 
que cada clase tenga una única responsabilidad siguiendo el principio de responsabilidad única (SRP). Además, el sistema debe incluir 
condicionales, ciclos y colecciones para manejar la lógica de los pedidos.
! Nivel de Complejidad: Media-Alta
    Estructura clara y modular: Se requiere diseñar varias clases con responsabilidades bien definidas.
    Interacción dinámica: El sistema debe permitir la entrada de datos en tiempo real con validaciones.
    Reglas de negocio con condiciones: Se aplican descuentos, validaciones y bonificaciones basadas en la lógica del negocio.
    Uso eficiente de colecciones: Se deben almacenar clientes, productos y pedidos de manera que se pueda acceder a ellos fácilmente.
    Flujo de trabajo realista: Se necesita manejar estados de pedidos y permitir actualizaciones en el sistema.
Todo Requisitos del sistema
#* 1. Gestión de Productos
    Cada producto del menú tiene un nombre, precio y categoría (ejemplo: entrada, plato fuerte, postre, bebida).
    Se debe almacenar el menú en una colección que permita acceder a los productos fácilmente.
    Debe existir una funcionalidad para agregar, actualizar y eliminar productos del menú (solo para administradores).
#* 2. Gestión de Pedidos
    Cada pedido tiene un número de pedido, cliente y una lista de productos.
    Se debe calcular el costo total del pedido sumando los precios de los productos seleccionados.
    Si el total del pedido supera los $100, se aplica un descuento del 10%.
    Si el cliente pide más de 5 productos, se le ofrece una bebida gratis.
    Los pedidos pueden tener diferentes estados: "Pendiente", "En preparación" y "Listo".
#* 3. Registro de Clientes
    Cada cliente tiene un nombre y número de contacto.
    Se debe validar que no haya clientes duplicados en el sistema.
    Si un cliente ya ha hecho más de 5 pedidos previos, se le da un descuento adicional del 5%.
#* 4. Procesamiento de Pedidos
    Cuando un cliente hace un pedido, se verifica que los productos existan en el menú.
    Se registra la hora en que se tomó el pedido.
    Una vez listo, se actualiza el estado del pedido a "Preparado".
    Se debe permitir cancelar pedidos antes de que entren en preparación.
#* 5. Menú interactivo para la administración
    Opción para registrar un nuevo cliente.
    Opción para agregar productos al menú (solo administradores).
    Opción para hacer un nuevo pedido.
    Opción para ver los pedidos en curso.
    Opción para marcar un pedido como listo.
    Opción para cancelar pedidos (si aún no están en preparación).
"""

import textwrap
from datetime import datetime

# Clase Producto (solo maneja productos del menu)
class Producto:
    def __init__(self, nombre, precio, categoria):
        self._nombre = nombre
        self._precio = precio
        self._categoria = categoria
   
# Clase Cleinte (solo maneja informacion de los clientes)     
class Cliente:
    def __init__(self, nombre, numero_contacto):
        self._nombre = nombre
        self._numero_contacto = numero_contacto
        self._pedidos_realizados = 0
    
# Clase Pedido (solo maneja pedidos)
class Pedido:
    estados = ['Pendiente', 'En preparacion', 'Listo']
    
    def __init__(self, numero_pedido, cliente, lista_produ):
        self._numero_pedido = numero_pedido
        self._cliente = cliente
        self._lista_produ = lista_produ
        self._hora_pedido = datetime.now()
        self._estado = 'Pendiente'
    
    def calcular_total(self):
        total = sum(p._precio for p in self._lista_produ)
        
        if total > 100:
            total *= 0.9
            
        if self._cliente._pedidos_realizados > 5:
            total *= 0.95

        return round(total, 2)
    
    def aplicacar_bonificacion(self):
        if len(self._lista_produ) > 5:
            bebida_gratis = Producto('Bebida gratis', 0, 'Bebida')
            self._lista_produ.append(bebida_gratis)

    def actualizar_estado(self, nuevo_estado):
        if nuevo_estado in self.estados:
            self._estado = nuevo_estado
        else:
            print('Estado invalido')
            
# Clase Restaurante (solo maneja la gestion del restaurante)
class Restaurante:
    def __init__(self):
        self._menu = {}
        self._clientes = {}
        self._pedidos = {}
        self._contador_pedidos = 1
        
    def agregar_productos(self, nombre, precio, categoria):
        self._menu[nombre] = Producto(nombre, precio, categoria)
        print(f"Producto '{nombre}' agregado al menu.")
    
    def registrar_cliente(self, nombre, telefono):
        if telefono in self._clientes:
            print('Cliente ya registrado')
            return

        self._clientes[telefono] = Cliente(nombre, telefono)
        print(f"Cliente '{nombre} registrado.'")

    def realizar_pedido(self, telefono, producto):
        if  telefono not in self._clientes:
            print("Cliente no encontrado. Registrelo primero")
            return
        
        cliente = self._clientes[telefono]
        producto_pedido = []

        for nombre_produ in producto:
            if nombre_produ in self._menu:
                producto_pedido.append(self._menu[nombre_produ])
            else:
                print(f"Producto '{nombre_produ}' no encontrado en el menu")

        if not producto_pedido:
            print('No de pudo crear el pedido. No hay productos validos')
            return 
        
        pedido = Pedido(self._contador_pedidos, cliente, producto_pedido)
        pedido.aplicacar_bonificacion()

        self._pedidos[self._contador_pedidos] = pedido
        cliente._pedidos_realizados += 1
        print(f"Pedido #{pedido._numero_pedido} creado para {cliente._nombre}. Total: ${pedido.calcular_total()}")

    def mostrar_pedidos(self):
        if not self._pedidos:
            print('No hay pedidos')
            return 
        
        print("\n\tPedidos en curso")
        for pedido in self._pedidos.values():
            print(f"Pedido #{pedido._numero_pedido}\nCliente: {pedido._cliente._nombre}\nEstado: {pedido._estado}\nTotal: ${pedido.calcular_total()}")
            
    def actualizar_estado_pedido(self, numero_pedido, nuevo_estado):
        if numero_pedido not in self._pedidos:
            print('Pedido no encontrado')
            return
        self._pedidos[numero_pedido].actualizar_estado(nuevo_estado)
        print(f"Pedido #{numero_pedido} actualizado a estado '{nuevo_estado}'")

    def cancelar_pedido(self, nuevo_pedido):
        if nuevo_pedido in self._pedidos and self._pedidos[nuevo_pedido].estado == 'Pendiente':
            del self._pedidos[nuevo_pedido]
            print(f"Pedido #{nuevo_pedido} cancelado")
        else:
            print("No se puede cancelar este pedido")

restaurante = Restaurante()

restaurante.agregar_productos("Pizza", 20, "Plato fuerte")
restaurante.agregar_productos("Hamburguesa", 15, "Plato fuerte")

while True:
    print(textwrap.dedent("""\
        1. Registrar al cliente
        2. hacer pedido
        3. Mostrar pedidos
        4. Cambiar estado de pedido
        5. Cancelar pedido
        6. Salir"""))

    opcion = int(input("Seleccione una opcion: "))

    match (opcion):
        case 1:
            nombre = input('Ingrese el nombre del cliente: ')
            telefono = input("Ingrese el telefono del cliente: ")
            restaurante.registrar_cliente(nombre, telefono)
        case 2:
            telefono = input('Ingrese el telefono del cliente: ')
            producto = input('Ingrese los porductos separados por coma: ').split(",")
            restaurante.realizar_pedido(telefono, producto)
        case 3:
            restaurante.mostrar_pedidos()
        case 4:
            numero_pedido = int(input("Ingrese el número de pedido: "))
            nuevo_estado = input("Ingrese el nuevo estado (Pendiente, En preparación, Listo): ")
            restaurante.actualizar_estado_pedido(numero_pedido, nuevo_estado)
        case 5:
            numero_pedido = int(input("Ingrese el número de pedido a cancelar: "))
            restaurante.cancelar_pedido(numero_pedido)
        case 6:
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")