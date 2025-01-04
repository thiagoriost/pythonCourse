class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount} en la cuenta de {self.account_holder}. Saldo actual {self.balance}")
        else:
            print(f"No se puede depositar, la cuenta {self.account_holder} esta inactiva")
    
    def wirhdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}, de la cuenta de {self.account_holder}, el saldo actual es {self.balance}")
    
    def deactivate_account(self):
        self.is_active = False
        print(f"Su cuenta {self.account_holder}, ha sido desactivada")
    
    def activate_account(self):
        self.is_active = True
        print(f"Su cuenta {self.account_holder}, ha sido activada")
        
account1 = BankAccount("Rigo", 500)
account2 = BankAccount("Ana", 1500)

# llamada a los metodos
account1.deposit(200)
account2.deposit(1200)

account1.deactivate_account()
account1.deposit(50)
