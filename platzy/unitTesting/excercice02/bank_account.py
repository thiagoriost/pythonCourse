from datetime import datetime
from exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta Creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Depsoted {amount}. New Balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        if now.hour < 8 and now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from to ")
        
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Withdrawal of {amount} exceeds balance {self.balance}"
            )
        
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New Balance: {self.balance}")            
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Balance: {self.balance}")        
        return self.balance
    
    def do_transfer(self, amount):
        if (amount > 0 and self.balance >= amount ):
            self.balance -= amount
        else:
            raise ValueError("Fondos insuficientes para esta transacción")
        
            
            
        return self.balance