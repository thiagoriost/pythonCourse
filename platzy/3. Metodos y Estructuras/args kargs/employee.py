class Employee:
    def __init__(self, name, *args, **kwargs):
        print(f"name => {name}, *args => {args}, **kwargs => {kwargs}")
        self.name = name
        self.skills = args
        self.details = kwargs
    
    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Skills', self.skills)
        print('Details', self.details)

employee = Employee('Carlos', 'Python', 'Java', 'C++', 'R', age=30, city = 'Bogotá', test = True)

employee.show_employee()