""" 
Métodos Mágicos en Python
1. Inicialización y Representación
__init__: Inicializa una nueva instancia.
__new__: Controla la creación de una instancia antes de inicializarla.
__del__: Ejecuta lógica al eliminar una instancia.
__repr__: Devuelve una representación formal del objeto.
__str__: Devuelve una representación informal legible del objeto.
2. Operadores Aritméticos
__add__: Suma (+).
__sub__: Resta (-).
__mul__: Multiplicación (*).
__truediv__: División (/).
__floordiv__: División entera (//).
__mod__: Módulo (%).
__pow__: Potencia (**).
__neg__: Negativo (-obj).
3. Operadores de Comparación
__eq__: Igualdad (==).
__ne__: Desigualdad (!=).
__lt__: Menor que (<).
__le__: Menor o igual que (<=).
__gt__: Mayor que (>).
__ge__: Mayor o igual que (>=).
4. Contenedores e Iteradores
__getitem__: Acceso por índice (obj[i]).
__setitem__: Asignación por índice (obj[i] = valor).
__delitem__: Eliminación por índice (del obj[i]).
__len__: Tamaño (len(obj)).
__iter__: Devuelve un iterador para el objeto.
__next__: Devuelve el siguiente elemento del iterador.
__contains__: Verifica si un elemento está contenido (x in obj).
5. Representaciones Numéricas
__int__: Conversión a entero (int(obj)).
__float__: Conversión a flotante (float(obj)).
__bool__: Conversión a booleano (bool(obj)).
6. Gestión de Contextos
__enter__: Lógica al entrar en un contexto (with obj:).
__exit__: Lógica al salir de un contexto.
7. Operadores Bit a Bit
__and__: AND bit a bit (&).
__or__: OR bit a bit (|).
__xor__: XOR bit a bit (^).
8. Manejo de Atributos
__getattr__: Acceso a atributos inexistentes.
__setattr__: Asignación de atributos (obj.attr = valor).
__delattr__: Eliminación de atributos (del obj.attr).
"""

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        # Devuelve una representación amigable para el usuario
        return f"Persona: {self.nombre}, {self.edad} años"

    def __repr__(self) -> str:
        # Devuelve una representación detallada del objeto para depuración
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

    def __eq__(self, otra_persona) -> bool:
        # Compara si dos personas son iguales en función del nombre y la edad
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

    def __lt__(self, otra_persona) -> bool:
        # Compara si una persona es "menor" que otra en función de la edad
        return self.edad < otra_persona.edad

    def __add__(self, otra_persona):
        # Sobrecarga el operador + para sumar las edades de dos personas
        return self.edad + otra_persona.edad

# Crear instancias de Persona
p1 = Persona("Ana", 28)
p2 = Persona("Luis", 35)
p3 = Persona("Ana", 28)

# __str__: Representación legible
# print(p1)  # Output: Persona: Ana, 28 años

# __repr__: Representación detallada
# print(repr(p2))  # Output: Persona(nombre='Luis', edad=35)

# __eq__: Comparación de igualdad
print(p1 == p3)  # Output: True (son iguales en nombre y edad)

# __lt__: Comparación "menor que" por edad
#print(p1 < p2)  # Output: True (porque 28 es menor que 35)

# __add__: Sumar edades de dos personas
# print(p1 + p2)  # Output: 63 (28 + 35)


""" 
1. ¿Qué es la Sobrecarga de Operadores?
Por defecto, los operadores en Python como + o == solo funcionan con tipos de datos predefinidos (números, cadenas, listas, etc.). Sin embargo, con la sobrecarga de operadores, podemos modificar cómo estos operadores funcionan con nuestras clases personalizadas.

Ejemplo básico de sobrecarga de +:
Imagina que tienes una clase Vector, y quieres sumar dos vectores usando el operador +. Para esto, usaremos el método mágico __add__.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = v1 + v2  # Sobrecarga de `+`
print(v3)  # Output: Vector(6, 4)

Aquí, __add__ define que la suma de dos objetos Vector es un nuevo Vector con la suma de sus componentes.

2. Sobrecarga de Comparación (==, <, >)
La sobrecarga no se limita a operadores aritméticos, también podemos redefinir operadores de comparación como ==, <, > para que comparen objetos en función de los atributos que queramos.

Ejemplo de sobrecarga de == para comparar objetos:

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otra_persona):
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

p1 = Persona("Ana", 30)
p2 = Persona("Ana", 30)

print(p1 == p2)  # Output: True (Ambas personas tienen el mismo nombre y edad)

En este caso, __eq__ permite que el operador == compare dos personas por sus atributos nombre y edad.

3. Ejemplo de Sobrecarga de Otros Operadores
Aparte de + y ==, otros operadores pueden ser sobrecargados, como el operador de resta -, multiplicación *, y operadores de comparación como <, >. Veamos un ejemplo de sobrecarga del operador de comparación <.

Ejemplo con el operador < (menor que):

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad

p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)

print(p1 < p2)  # Output: True (Ana es menor que Luis)


Aquí, __lt__ permite comparar las edades de dos personas con el operador <.

4. Buenas Prácticas al Sobrecargar Operadores
Usa la sobrecarga cuando tenga sentido: No abuses de la sobrecarga de operadores. Solo la utilices cuando sea intuitivo y claro que un operador debe funcionar con tus clases.
Mantén la consistencia: Si sobrecargas un operador como +, asegúrate de que el comportamiento sea consistente con lo que los usuarios esperan (por ejemplo, que la suma de dos vectores realmente sume sus componentes).
Documenta el comportamiento: Aunque la sobrecarga de operadores puede hacer que tu código sea más limpio, es importante que documentes claramente cómo se comportan los operadores sobrecargados, especialmente si tienen un comportamiento no convencional.
5. Ejercicio Práctico: Sobrecargar el Operador + en una Clase de Fracciones
Objetivo: Implementa una clase Fraccion que permita sumar fracciones usando el operador +.

Requerimientos:
La clase debe tener numerador y denominador.
El operador + debe sumar dos fracciones y devolver el resultado simplificado.

from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, otra_fraccion):
        nuevo_num = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
        nuevo_den = self.denominador * otra_fraccion.denominador
        comun_divisor = gcd(nuevo_num, nuevo_den)
        return Fraccion(nuevo_num // comun_divisor, nuevo_den // comun_divisor)

    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"

f1 = Fraccion(1, 4)
f2 = Fraccion(1, 2)

f3 = f1 + f2  # Suma de fracciones
print(f3)  # Output: 3/4

# Este ejemplo muestra cómo redefinir el operador + para sumar fracciones de manera intuitiva.
"""