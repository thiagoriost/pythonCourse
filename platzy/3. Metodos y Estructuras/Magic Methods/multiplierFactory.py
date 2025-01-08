class MultiplierFactory:
    
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        return super(MultiplierFactory, cls).__new__(cls)
    
    def __init__(self, factor: int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor
    
    def __call__(self, number: int) -> int:
        print("number => ", number)
        print("self.factor => ", self.factor)
        return number * self.factor
    
multiplier = MultiplierFactory(5)

result = multiplier(10)
print(result)