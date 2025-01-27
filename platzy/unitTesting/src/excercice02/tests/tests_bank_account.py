import unittest, os

from bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    """ Este metodo setUp siempre se ejecuta antes de cada prueba"""
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")
        
    """ Este metodo tearDown siempre se ejecuta despues de cada prueba"""
    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file) # borra el archivo de log cread

    def _count_lines(self, file):
        with open(file, "r") as f:
            return len(f.readlines())
        
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800
    
    def test_get_balance(self):
        assert self.account.get_balance() == 1000
        
    def test_do_transfer_1(self):
        assert self.account.do_transfer(300) == 700
        
    def test_do_transfer_2(self):
        assert self.account.do_transfer(1000) == 0
        
    def test_successful_transfer(self):
        """Prueba una transferencia exitosa."""
        self.account.do_transfer(50)
        self.assertEqual(self.account.balance, 950)

    def test_insufficient_funds(self):
        # Prueba una transferencia con fondos insuficientes.
        with self.assertRaises(ValueError) as context:
            self.account.do_transfer(1150)
        self.assertEqual(str(context.exception), "Fondos insuficientes para esta transacción")

    def test_negative_transfer(self):
        # Prueba una transferencia con un monto negativo.
        with self.assertRaises(ValueError) as context:
            self.account.do_transfer(-10)
        self.assertEqual(str(context.exception), "Fondos insuficientes para esta transacción") 
        
    def test_transaction_log(self):
       self.account.deposit(500)
       assert os.path.exists("transaction_log.txt")
       
    def test_count_transactions(self)       :
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
