import unittest
# import platzy.unitTesting.src.excercice02.tests.tests_bank_account.BankAccountTests
# from tests_bank_account import BankAccountTests
from test_bank_account import BankAccountTests  # Ajusta la ruta

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite
    
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
    