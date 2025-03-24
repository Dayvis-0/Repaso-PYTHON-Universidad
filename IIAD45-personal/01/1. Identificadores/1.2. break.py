"""En la clase CajaRegistradora, el método procesar_compra debe:

Pedir al usuario que ingrese el precio de un artículo uno por uno.

Calcular y mostrar el total acumulado de la compra después de cada entrada.

Detenerse si el usuario ingresa un precio negativo o cero, utilizando el identificador break.

Al finalizar la entrada de datos, mostrar el total final de la compra."""

class CajaRegistradora:
    # Clase que registra ela compra del usuario
    
    def __init__(self):
        # Pedir al usuario el precio de una compra
        
        self._total = 0
        
    def agre_pre(self, precio):
        # Agregar el precio a la compra
        
        if precio > 0:
            self._total += precio
        
        else:
            print('Precio de invalido. No se agregara al total.')
    
    def mostrar(self):
        # Mostrar el monto de la compra realizada
        
        print(f'Total acumulado: {self._total:.2f}')
        
    def proce_comp(self):
        
        while True:
            try:
                precio = float(input('Precio del articulo (negativo o cero para finalizar): '))
                if precio <= 0:
                    break
                
                self.agre_pre(precio)
                self.mostrar()
                    
            except ValueError:
                print('Entrada invalida. Ingrese un numero')
        
        print(f'\nCompra finalizada. Total a pagar: {self._total:.2f}')

caja = CajaRegistradora()

caja.proce_comp()