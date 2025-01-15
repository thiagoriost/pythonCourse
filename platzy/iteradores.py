#ejemplo
# Crear lista
my_list=list(range(1,5))
print(my_list)
# obtener iterador
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#  ...
print("////////// Iterar en cadena //////////")
text = "hola mundo"
iter_text = iter(text)
for e in iter_text:
    print(e)

print("///////// iterar numeros impares //////////")
limit = 10
odd_itter = iter(range(1, limit+1, 2))
for num in odd_itter:
    print(num)
print("///////// iterar numeros pares //////////")
limit = 10
odd_itter = iter(range(0, limit+1, 2))
for num in odd_itter:
    print(num)

print("///////// Generador //////////")
def my_generador():
    yield 1
    yield 2
    yield 3

for e in my_generador():
    print(e)

print("///////// Serie de Fibonachi  /////////////////")
def fibonacci(limit):
    a, b = 0, 1
    # lo anterior es lo mismo q
    # a = 0
    # b = 1
    while a<limit:
        yield a
        a, b = b, a+b
        # lo anterior es lo mismo q
        # a = b
        # b = a + b

for e in fibonacci(10):
    print(e)
  