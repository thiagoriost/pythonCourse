class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self, text="persona"):
        print(f"Hello! I am a {text}.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def greet(self):
        super().greet(f"Estudiante con id = {self.student_id}")
        # print("Hello! I am a person.")

pers1 = Student("Rigo", 35, 2134)
pers1.greet()

pers2 = Person("Ana", 25)
pers2.greet()