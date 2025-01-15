def divide(a: int, b: int) -> float:
    #validar qeu ambos parametros sean enteros
    if not isinstance(a,int) or not isinstance(b, int):
        raise TypeError('Ambos parámetros deben ser enteros.')
    
    #Verificamos que el divisor no sea cero
    if b ==0:
        raise ValueError('El divisor no puede ser cero.')
    
    return a/b

#Ejemplo de uso
try:
    res = divide(10,'2') #Error de tipo
    print(res)
except TypeError as e:
    print(f'Error: {e}')

#Ejemplo de uso
try:
    res = divide(10,0) #Error de división por cero
    print(res)
except ValueError as e:
    print(f'Error: {e}')

#Ejemplo de uso
try:
    res = divide(10,2) #División correcta
    print(res)
except (ValueError, TypeError) as e:
    print(f'Error: {e}')
    
try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)
    
try:
    assert 1 != 1, 'Uno no es igual a 1'
except AssertionError as error:
    print(error)


try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)


print("-"*30)
try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
    assert 1 != 1, 'Uno no es igual a 1'
    print(0/0)
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print("Continua con la ejecucion del programa")


def my_divide(a, b):
   # Escribe tu solución 👇
   try:
        result = a / b
        return int(result)
   except ZeroDivisionError as e:
       return 'No se puede dividir por 0'
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0