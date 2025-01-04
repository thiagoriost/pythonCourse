print("//////// factorial de un numero n! ////////////")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(7))

print("//////// serie de fibonacci ////////////")

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

print("//////// suma de numeros naturales ////////////")

def sumaNumNatur(n):
    
    if n == 0:
        return 0
    else:
        return n+sumaNumNatur(n - 1)
print(sumaNumNatur(5))