id1:int = 101
id2:int = 102
totalId: int = id1 + id2
# ---------------------------------------
def add_emplotesIds(id1: int, id2: int)  -> int:
    return id1 + id2

print(add_emplotesIds(3, 5))

print("--------------------------------------")
class Employee:
    name: str
    age: int
    salary: float
    
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
        
    def introduce(self) -> str:
        return f"Hi my name is {self.name}, ..."
    
emplo1 = Employee("Rigo", 43, 5000)
print(emplo1.introduce())

print("--------------------------------------")

from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Parámetros:
    employee_ids (list[int]): Lista de IDs de empleados.
    employee_id (int): ID a buscar.

    Retorna:
    Optional[int]: El ID encontrado o None si no existe en la lista.
    """
    if employee_id in employee_ids:
        return employee_id
    return None

print("--------------------------------------")

from typing import Union

def process_salary(salary: Union[int, float]) -> float:
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario convertido a flotante.
    """
    return float(salary)

print("--------------------------------------")

def lista_empleados(lista_empleados:list, limite_salario:float)-> list:
    return [emp['nombre'] for emp in lista_empleados if emp['sueldo'] > limite_salario]


lista = [
    {"nombre": "Maria La del Barrio",
     "edad": 30,
     "sueldo": 30000
     },
    {"nombre": "Luis Miguel",
     "edad": 25,
     "sueldo": 25000
     },
    {"nombre": "Ana Bolena",
     "edad": 20,
     "sueldo": 20000
     },
     {"nombre": "Pepe Grillo",
     "edad": 20,
     "sueldo": 50000
     }
]

print(lista_empleados(lista, 25000))

print("--------------------------------------")

def divide(a: int, b: int) -> float:
    # valida q ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos parametros debe ser enteros o flotantes')
        # return None
    #Verificar q el divisor no sea cero
    if b == 0:
        raise TypeError('El divisor no puede ser cero')
        return None # con lo anterior ya no ejecuta esta linea
    return a/b

res_q = print(divide('5', 10))

try:
    res = divide(10,'2') # error de tipo a drede
    print(res)
except TypeError as e:
    print(f'Error: {e}')

print("--------------------------------------")



print("--------------------------------------")


