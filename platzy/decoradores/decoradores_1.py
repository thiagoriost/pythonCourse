
print("11111111111")
def log_transaction(my_func):
    print("33333")
    def wraper():
        print(f"55555 Log de la transaccion...")
        my_func()
        print(f"77777 Los terminados...")
    return wraper

print("2222222222222")

@log_transaction
def process_payment():
    print('66666 Procesando pago...')

print("4444")
process_payment()
print("88888")