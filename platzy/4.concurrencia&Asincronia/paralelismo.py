import multiprocessing

#Función que calcule el cuadrado de un número
def calculate_square(n):
    return n*n

if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    #crear un pool
    with multiprocessing.Pool() as pool: # para ejecutar hilos en paralelo
        results = pool.map(calculate_square, numbers) # con el pool se ejecutan todos los flujos en forma paralela

    print(f'Resultados: {results}')
    
""" 
2. Compartir Datos entre Procesos con multiprocessing
A diferencia de los hilos, los procesos no comparten memoria de forma predeterminada. Para que dos procesos puedan compartir datos, Python proporciona herramientas como multiprocessing.Queue y multiprocessing.Value.

Ejemplo: Compartir Datos con Queue en multiprocessing
"""

def calcular_cuadrado(numeros, cola):
    for n in numeros:
        cola.put(n * n)

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    cola = multiprocessing.Queue()

    proceso = multiprocessing.Process(target=calcular_cuadrado, args=(numeros, cola))
    proceso.start()
    proceso.join()

    # Extraer resultados de la cola
    while not cola.empty():
        print(cola.get())
        
""" 
Explicación:

Usamos Queue para que el proceso secundario pueda pasar datos de vuelta al proceso principal.
"""

""" 
4. Coordinación de Tareas con multiprocessing.Manager
Cuando los procesos deben compartir estructuras de datos complejas (como listas o diccionarios), 
podemos usar un Manager para crear un espacio de memoria compartido entre procesos.

Ejemplo: Uso de Manager para Compartir Listas entre Procesos

"""

def agregar_valores(lista_compartida):
    for i in range(5):
        lista_compartida.append(i)

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        lista_compartida = manager.list()

        proceso1 = multiprocessing.Process(target=agregar_valores, args=(lista_compartida,))
        proceso2 = multiprocessing.Process(target=agregar_valores, args=(lista_compartida,))

        proceso1.start()
        proceso2.start()

        proceso1.join()
        proceso2.join()

        print(f"Lista compartida: {lista_compartida}")

""" 
Explicación:

multiprocessing.Manager nos permite crear una lista compartida entre varios procesos, 
facilitando la comunicación entre ellos.
"""