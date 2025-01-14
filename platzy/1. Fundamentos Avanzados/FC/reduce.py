from functools import reduce

""" 
result = reduce(function, iterable, [initializer])

function: Una función que toma dos argumentos y devuelve un único valor.
iterable: Una secuencia (lista, tupla, etc.) cuyos elementos se procesarán.
initializer (opcional): Un valor inicial para empezar el cálculo.
"""

numbers = [5, 5, 1, 4, 5]

# Suma acumulativa
result = reduce(lambda x, y: x + y, numbers)
print("result => ", result)  # Salida: 15


numbers = list(range(1,5))
print(numbers)

def accum(count, item) :
    print("count => ", count)
    print("item => ", item)
    return count + item


result = reduce(accum, numbers)
print("result => ", result)