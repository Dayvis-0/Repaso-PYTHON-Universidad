from TarjetaDeCredito import CreditCard

class PredatoryCreditCard(CreditCard):
    """Una extension de Trejeta de Credito que combra itereses e impuestos"""
    
    def __init__(self, customer, bank, account, limit, interest):
        super().__init__(customer, bank, account, limit)
        self._interest = interest
        
    def charge(self, price):
        """Cargar el precio dado en la tarjeta, asumiendo que hay credito
        
        Devuelve True si el cargo procede
        Devuelve Falso y cobra $5 de impuesto si el cargo es denegado"""
        
        success = super().charge(price)
        
        if not success:
            self._balance += 5
            
        return success
    
    def monthly_process(self):
        """Asigna un interes mensual sobre el balance"""
        
        if self._balance > 0:
            monthly_factor = pow(1 + self._interest, 1/12)
            
            self._balance *= monthly_factor
            
if __name__ == '__main__':
                
    pcc = PredatoryCreditCard("Juan", "Banco XYZ", "1234", 5000, 0.05)
    print(pcc._balance)  