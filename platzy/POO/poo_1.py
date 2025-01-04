class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")


persona1 = Person("Rigo", 42)
persona2 = Person("Ana", 32)

persona1.greet()
persona2.greet()
