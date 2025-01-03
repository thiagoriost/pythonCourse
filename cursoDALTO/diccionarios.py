numeros = {1:"uno",2:"dos",3:"tres"}
print(numeros)
print(numeros[2])
informacion = {'nombre': "Rigo", 'edad': 45}
print(informacion)
# del informacion["edad"]
# print(informacion)
claves = informacion.keys()
print("claves => ", claves)
print(type(claves))
values = informacion.values()
print("values => ", values)
pares = informacion.items()
print("pares => ", pares)
contactos = {
    'rigo': {
        
        'altura': 1.85,
        'edad': 45
    },
    'Ana': {        
        'altura': 1.65,
        'edad': 35
    }}
print(contactos)
print(contactos['Ana'])