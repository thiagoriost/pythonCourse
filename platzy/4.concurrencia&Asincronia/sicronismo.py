""" 
1. Sincronización de Hilos en Python
Cuando varios hilos intentan acceder a un mismo recurso al mismo tiempo, pueden ocurrir problemas de coherencia. Para evitar esto, se utilizan mecanismos de sincronización, como Lock y RLock, que garantizan que solo un hilo acceda a un recurso crítico a la vez.

Ejemplo: Uso de Lock para Evitar Condiciones de Carrera
"""

import threading

# Variable compartida
saldo = 0
lock = threading.Lock()  # Crear un Lock

def depositar(dinero):
    global saldo
    for _ in range(100000):
        with lock:  # Bloquear el acceso para evitar condiciones de carrera
            saldo += dinero

hilos = []
for _ in range(2):
    hilo = threading.Thread(target=depositar, args=(1,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"Saldo final: {saldo}")  # Esperamos ver 200000 como saldo

""" 
Explicación:

El uso de Lock asegura que solo un hilo modifique la variable saldo en un momento dado, 
evitando que el resultado final sea incorrecto.
"""


""" 
3. Problemas de Sincronización y Cómo Evitarlos
A medida que manejas tareas más complejas, es posible que te encuentres con problemas como deadlocks y race conditions. Entender estos problemas es crucial para escribir código concurrente robusto.

Evitar Deadlocks con RLock
Un deadlock ocurre cuando dos o más hilos se bloquean mutuamente al esperar por un recurso que está siendo utilizado por otro hilo. Para evitar esto, podemos usar RLock en lugar de Lock.

Ejemplo: Uso de RLock para Evitar Deadlocks
"""


class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        self.lock = threading.RLock()

    def transferir(self, otra_cuenta, cantidad):
        with self.lock:
            self.saldo -= cantidad
            otra_cuenta.depositar(cantidad)

    def depositar(self, cantidad):
        with self.lock:
            self.saldo += cantidad

cuenta1 = CuentaBancaria(500)
cuenta2 = CuentaBancaria(300)

hilo1 = threading.Thread(target=cuenta1.transferir, args=(cuenta2, 200))
hilo2 = threading.Thread(target=cuenta2.transferir, args=(cuenta1, 100))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"Saldo cuenta1: {cuenta1.saldo}")
print(f"Saldo cuenta2: {cuenta2.saldo}")

""" 
Explicación:

Usamos RLock para evitar que múltiples operaciones simultáneas en una cuenta causen bloqueos.
"""