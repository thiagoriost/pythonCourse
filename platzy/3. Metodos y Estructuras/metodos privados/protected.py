class BaseClass:
    def __init__(self):
        self._protected_variableRRH = 'Protected'
        self.__private_variable = 'Private'

    def _protected_method_RRH(self):
        print('Este es un metodo protegido')

    def __private_method(self):
        print('Esto es un metodo privado')

    def public_method(self):
        self.__private_method()

base = BaseClass()
print(base._protected_variableRRH)
base._protected_method_RRH()

base.public_method() # este metodo invocara al privado ya q no se puede directamente 
# print(base.__private_variable)
# print(base.__private_method())