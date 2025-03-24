class CreditCard:
    def __init__(self, customer, bank, account, limit, balance = 0):
        self._customer = customer  
        self._bank = bank 
        self._account = account
        self._limit = limit 
        self._balance = balance
        
    def get_customer(self): return self._customer
    
    def get_bank(self): return self._bank
        
    def get_account(self): return self._account
    
    def get_limit(self): return self._limit
    
    def get_balance(self): return self._balance
    
    def charge(self, price):
        
        if not isinstance(price,(int, float)):
            raise ValueError('It is not a numerical value')
        
        if price + self._balance > self._limit:
            
            return False
        else:
            
            self._balance += price
            return True
        
    def pay(self, amount):
        
        if not isinstance(amount, (int, float)):
            
            raise ValueError('It is not a numerical value')
        
        self._balance -= amount
        
wallets = []

wallets.append(CreditCard('Dayvis','BCP','1234 5678 9103',2500))
wallets.append(CreditCard('Maria','VDA','1213 2123 3122',1500,101))

for val in range(1,2):
    wallets[0].charge(val)
    wallets[1].charge(val*2)
    
for i in range(len(wallets)):
    print(f'Customer = {wallets[i].get_customer()}')
    print(f'Bank = {wallets[i].get_bank()}')
    print(f'Account = {wallets[i].get_account()}')
    print(f'Limit = {wallets[i].get_limit()}')
    print(f'Balance = {wallets[i].get_balance()}')
    
    while wallets[i].get_balance() > 100:
        wallets[i].pay(100)
        
        print(f'New balance = {wallets[i].get_balance()}')
    print()