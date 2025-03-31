"""El encapsulamiento es el principio de ocultar los detalles internos de un ubjeto y restringir el acceso directo a sus datos, permitiendo la 
interaccion solo a traves de metodos definidos. Esto ayuda a proteger la integridad del objeto  y a mantener un bajo acoplamiento entre componentes"""

class BankAccount:
    def __init__(self, du, ba = 0):
        self.owner = du
        self.__balance = ba
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
    def whitdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -=amount
            
    def get_balance(self):
        
        return self.__balance
    
account = BankAccount('Dayvis',1000)

account.deposit(100)
account.whitdraw(200)

print(account.get_balance())