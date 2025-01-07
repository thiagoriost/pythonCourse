from collections import deque

def manage_delivery_queue() -> deque:
    # Crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    delivery_queue.append("order_4")  # Agrega al final de la cola
    delivery_queue.appendleft("order_0")  # Agrega al principio de la cola
    delivery_queue.pop()  # Elimina del final
    delivery_queue.popleft()  # Elimina del principio
    return delivery_queue

queue = manage_delivery_queue()
print(queue) 

""" 
deque (double-ended queue) es una estructura de datos en Python, proporcionada por el módulo collections, 
que permite operaciones rápidas de inserción y eliminación en ambos extremos de la cola. Es especialmente 
útil cuando se necesitan colas o pilas con un mejor rendimiento en comparación con las listas estándar para 
operaciones en los extremos.

Características principales de deque
Doble acceso:
Permite agregar o eliminar elementos tanto al inicio como al final de la cola.
Eficiencia:
Las operaciones en los extremos (append, appendleft, pop, popleft) son O(1).
Comparativamente, las operaciones de inserción/eliminación en los extremos de una lista estándar son menos eficientes
debido a la realocación de memoria.
Métodos adicionales:
Métodos como rotate, extend, extendleft y clear, que no están disponibles para listas estándar.
Uso común de deque
Implementar colas (FIFO) y pilas (LIFO).
Procesamiento eficiente de datos en ventanas deslizantes o buffers circulares.
Métodos principales
Método	Descripción
append(x)	Agrega el elemento x al final.
appendleft(x)	Agrega el elemento x al inicio.
pop()	Elimina y devuelve el último elemento.
popleft()	Elimina y devuelve el primer elemento.
extend(iterable)	Agrega elementos de un iterable al final.
extendleft(iterable)	Agrega elementos de un iterable al inicio (en orden inverso).
rotate(n)	Rota los elementos n pasos hacia la derecha (izquierda si n es negativo).
clear()	Elimina todos los elementos.
Ventajas sobre listas

"""

from collections import deque

# Crear una deque
dq = deque([1, 2, 3])

# Agregar elementos
dq.append(4)        # Agrega al final
dq.appendleft(0)    # Agrega al inicio

# Eliminar elementos
dq.pop()            # Elimina del final
dq.popleft()        # Elimina del inicio

# Imprimir la deque resultante
print(dq)  # Salida: deque([1, 2, 3])