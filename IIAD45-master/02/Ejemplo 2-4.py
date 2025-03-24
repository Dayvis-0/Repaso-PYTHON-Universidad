from TarjetaCredito import TarjetaCredito

class TarjetaCreditoDepredadora(TarjetaCredito):
    """Una extension de TajetaCredito que cobra intereses e impuestos"""
    
    def __init__(self, cliente, banco, cuenta, limite, interes):
        """Crea una instancia de una nueva tarjeta de credito depredadora
        
        interes:    tasa de interes (p.ej  0.05 para el 5%)
        """
        
        super().__init__(cliente, banco, cuenta, limite)
        self._interes = interes
        
    def cargar(self, precio):
        """Carga el precio dado en la tarjeta, asumiendo que hay credito
        
        Devuelve True si el cargo procede
        Devuelve Falso y cobra $5 de impuesto si el cargo es denegado"""
        
        exito = super().cargar(precio)
        if not exito:
            self._balance += 5
        return exito
    
    def proceso_mensual(self):
        """Asigna un interes mensual sobre el balance"""
        if self._balance > 0:
            factor_mensual = pow(1 + self._interes, 1/12)
            self._balance *= factor_mensual