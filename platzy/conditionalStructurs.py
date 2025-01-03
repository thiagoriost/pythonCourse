x = input("Ingresa X: ")

# Convertir la entrada a un número entero o flotante
try:
    x = float(x)  # Usa `int(x)` si esperas solo números enteros
    if not x > 5:
        print("X no es mayor q 5=>", x)
    if x > 5:
        print("X =>", x)
    elif x < 5:
        print("X es menor a 5")
    else:
        print("X es igual a 5")
except ValueError:
    print("Error: Ingresa un número válido.")
    
Y = input("Ingresa Y: ")

# Convertir la entrada a un número entero o flotante
try:
    Y = int(Y)  # Usa `int(Y)` si esperas solo números enteros
    if Y > 5:
        print("Y =>", Y)
    else:
        print("Y es menor o igual a 5")
except ValueError:
    print("Error: Ingresa un número válido.")
    
if x > 10 and Y > 25:
    print("x > 10 and Y > 25")

if x > 10 or Y > 25:
    print("x > 10 or Y > 25")
    

is_member = True
age = 15

if is_member:
    if age >= 15:
        print('all is ok')
    else:
        print("all isn't ok")
else:
    print('you are not member')