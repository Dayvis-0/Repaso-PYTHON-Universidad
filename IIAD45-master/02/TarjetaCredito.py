class TarjetaCredito:
    """Una terjeta de credito de cliente."""

    def __init__(self, cliente, banco, cuenta, limite):
        """Crea una instancia de tarjeta de credito

        EL balance inicial es cero

        cliente   el nombre del cliente (e.g., 'John Bowman')
        banco     el nombre del banco (e.g., 'California Savings')
        cuenta    el numero de tarjeta (e.g., '5391 0375 9387 5309')
        limite    limite de la tarjeta (en soles)
        """
        self._cliente = cliente
        self._banco = banco
        self._cuenta = cuenta
        self._limite = limite
        self._balance = 0

    def get_cliente(self):
        """Devuelve el nombre del cliente."""
        return self._cliente

    def get_banco(self):
        """Devuelve el nombre del banco."""
        return self._banco

    def get_cuenta(self):
        """Devuelve el numero de tarjeta (almacenado como cadena)."""
        return self._cuenta

    def get_limite(self):
        """Devuelve el limite de la tarjeta de credito."""
        return self._limite

    def get_balance(self):
        """Devuelve el balance actual."""
        return self._balance

    def cargar(self, precio):
        """Carga el precio dado a la tarjeta asumiendo que tiene saldo.

        Devuelve True si se pudo cargar y False si no se pudo.
        """
        if precio + self._balance > self._limite:  
            return False                           
        else:
            self._balance += precio
            return True

    def pagar(self, monto):
        """Procesa el pago del cliente y lo descuenta del balance."""
        self._balance -= monto
