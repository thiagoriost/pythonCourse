""" List comprehension
resultado = [ecuacion_a_aplicar_sobre_cada_lemento for e in my_lista filtro(opcional)]

ejemplo =  [i*2 for i in range(1,101) if i % 2 == 0]
"""

# imprime los cuadros de una lista de numeros del 1 al 5

print([x**2 for x in list(range(1,6))])

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

number = []
for e in range(1, 11):
    number.append(e * 2)
    
print(number)
number2 = [e * 2  for e in range(1,11)]
print(number2)

ejemplo =  [i*2 for i in range(1,101) if i % 2 == 0]
print(ejemplo)