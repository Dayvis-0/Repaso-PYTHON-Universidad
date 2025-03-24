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
    if not isinstance(precio, (int,float)):
        raise ValueError("No es un valor numerico")
    
    if precio + self._balance > self._limite:  
      return False                           
    else:
      self._balance += precio
      return True

  def pagar(self, monto):
    """Procesa el pago del cliente y lo descuenta del balance."""
    
    if not isinstance(monto, (int,float)):
        raise ValueError("No es un valor numerico")
    self._balance -= monto

if __name__ == '__main__':
  billetera = []
  billetera.append(TarjetaCredito('Ivan Soria', 'BCP',
                           '5391 0375 9387 5309', 2500) )
  billetera.append(TarjetaCredito('Ivan Soria', 'BBVA',
                           '3485 0399 3395 1954', 3500) )
  billetera.append(TarjetaCredito('Ivan Soria', 'BN',
                           '5391 0375 9387 5309', 5000) )

  for val in range(1, 17):
    billetera[0].cargar(val)
    billetera[1].cargar(2*val)
    billetera[2].cargar(3*val)

  for c in range(len(billetera)):
    print('Cliente =', billetera[c].get_cliente())
    print('Banco =', billetera[c].get_banco())
    print('Cuenta =', billetera[c].get_cuenta())
    print('Limite =', billetera[c].get_limite())
    print('Balance =', billetera[c].get_balance())
    while billetera[c].get_balance() > 100:
      billetera[c].pagar(100)
      print('Nuevo balance =', billetera[c].get_balance())
    print()
