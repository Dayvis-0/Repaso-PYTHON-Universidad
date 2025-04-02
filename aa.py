from datetime import datetime

# Clase Producto (únicamente maneja productos del menú)
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

# Clase Cliente (únicamente maneja información de clientes)
class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.pedidos_realizados = 0  # Contador de pedidos para aplicar descuentos

# Clase Pedido (únicamente maneja pedidos)
class Pedido:
    ESTADOS = ["Pendiente", "En preparación", "Listo"]

    def __init__(self, numero_pedido, cliente, productos):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.productos = productos
        self.hora_pedido = datetime.now()
        self.estado = "Pendiente"

    def calcular_total(self):
        total = sum(p.precio for p in self.productos)

        # Aplicar descuento si el total supera $100
        if total > 100:
            total *= 0.9  # Descuento del 10%

        # Aplicar descuento adicional si el cliente ha hecho más de 5 pedidos
        if self.cliente.pedidos_realizados > 5:
            total *= 0.95  # Descuento adicional del 5%

        return round(total, 2)

    def aplicar_bonificaciones(self):
        if len(self.productos) > 5:
            bebida_gratis = Producto("Bebida Gratis", 0, "Bebida")
            self.productos.append(bebida_gratis)

    def actualizar_estado(self, nuevo_estado):
        if nuevo_estado in self.ESTADOS:
            self.estado = nuevo_estado
        else:
            print("Estado inválido.")

# Clase Estacionamiento (únicamente maneja la gestión del restaurante)
class Restaurante:
    def __init__(self):
        self.menu = {}  # Diccionario de productos disponibles
        self.clientes = {}  # Diccionario de clientes registrados
        self.pedidos = {}  # Diccionario de pedidos en curso
        self.contador_pedidos = 1  # Generador de números de pedido

    def agregar_producto(self, nombre, precio, categoria):
        self.menu[nombre] = Producto(nombre, precio, categoria)
        print(f"Producto '{nombre}' agregado al menú.")

    def registrar_cliente(self, nombre, telefono):
        if telefono in self.clientes:
            print("Cliente ya registrado.")
            return
        self.clientes[telefono] = Cliente(nombre, telefono)
        print(f"Cliente '{nombre}' registrado.")

    def realizar_pedido(self, telefono_cliente, productos_solicitados):
        if telefono_cliente not in self.clientes:
            print("Cliente no encontrado. Regístrelo primero.")
            return

        cliente = self.clientes[telefono_cliente]
        productos_pedido = []

        for nombre_producto in productos_solicitados:
            if nombre_producto in self.menu:
                productos_pedido.append(self.menu[nombre_producto])
            else:
                print(f"Producto '{nombre_producto}' no encontrado en el menú.")

        if not productos_pedido:
            print("No se pudo crear el pedido. No hay productos válidos.")
            return

        pedido = Pedido(self.contador_pedidos, cliente, productos_pedido)
        pedido.aplicar_bonificaciones()

        self.pedidos[self.contador_pedidos] = pedido
        cliente.pedidos_realizados += 1  # Aumenta el contador de pedidos del cliente
        print(f"Pedido #{pedido.numero_pedido} creado para {cliente.nombre}. Total: ${pedido.calcular_total()}")
        self.contador_pedidos += 1

    def mostrar_pedidos(self):
        if not self.pedidos:
            print("No hay pedidos en curso.")
            return

        print("\nPedidos en curso:")
        for pedido in self.pedidos.values():
            print(f"Pedido #{pedido.numero_pedido} - Cliente: {pedido.cliente.nombre} - Estado: {pedido.estado} - Total: ${pedido.calcular_total()}")

    def actualizar_estado_pedido(self, numero_pedido, nuevo_estado):
        if numero_pedido not in self.pedidos:
            print("Pedido no encontrado.")
            return
        self.pedidos[numero_pedido].actualizar_estado(nuevo_estado)
        print(f"Pedido #{numero_pedido} actualizado a estado '{nuevo_estado}'.")

    def cancelar_pedido(self, numero_pedido):
        if numero_pedido in self.pedidos and self.pedidos[numero_pedido].estado == "Pendiente":
            del self.pedidos[numero_pedido]
            print(f"Pedido #{numero_pedido} cancelado.")
        else:
            print("No se puede cancelar este pedido.")

# Menú interactivo
restaurante = Restaurante()

# Agregamos algunos productos al menú
restaurante.agregar_producto("Pizza", 20, "Plato Fuerte")
restaurante.agregar_producto("Hamburguesa", 15, "Plato Fuerte")
restaurante.agregar_producto("Papas Fritas", 5, "Entrada")
restaurante.agregar_producto("Refresco", 3, "Bebida")

while True:
    print("\n1. Registrar cliente")
    print("2. Hacer pedido")
    print("3. Mostrar pedidos")
    print("4. Cambiar estado de pedido")
    print("5. Cancelar pedido")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        restaurante.registrar_cliente(nombre, telefono)

    elif opcion == "2":
        telefono = input("Ingrese el teléfono del cliente: ")
        productos = input("Ingrese los productos separados por coma: ").split(", ")
        restaurante.realizar_pedido(telefono, productos)

    elif opcion == "3":
        restaurante.mostrar_pedidos()

    elif opcion == "4":
        numero_pedido = int(input("Ingrese el número de pedido: "))
        nuevo_estado = input("Ingrese el nuevo estado (Pendiente, En preparación, Listo): ")
        restaurante.actualizar_estado_pedido(numero_pedido, nuevo_estado)

    elif opcion == "5":
        numero_pedido = int(input("Ingrese el número de pedido a cancelar: "))
        restaurante.cancelar_pedido(numero_pedido)

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
