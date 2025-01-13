import random

""" 
{key: value for i in iterable [opcional if condition]}

"""
diccionario_1 = {}

for i in range(1,11):
    diccionario_1[i] = i * 2
    
print("diccionario_1 tradicional=> ", diccionario_1)
print(" ----------------------- ")

diccionario_2 = { i: i*2 for i in range(1,11)}
print("diccionario_2 => de forma comprehention", diccionario_2)
print(" ----------------------- ")

diccionario_3 = { i: i*2 for i in range(1,11) if i < 10}
print("diccionario_3 con filtro => ", diccionario_3)

""" 
diccionario apartir de una lista
"""

countries = ["col", "mex", "bol", "pe"]
print("countries => ", countries)
population_1 = {}
for nameCountry in countries:
    population_1[nameCountry] = random.randint(100 , 10000)
print("population_1 => ", population_1)

population_2 = { i: random.randint(100 , 5000) for i in countries}
print("population_2 => ", population_2)

print(" ----------------------- ")
names = ['nico', 'zule','santi']
ages = [12,56,98]

""" {
    'nico':12,
    'zule': 56,
    'santi': 98
} """
""" Union entre listas """
print("names => ", names)
print("ages => ", ages)
unionListToFormDictionari = list(zip(names, ages))
""" lo anterior generar una lista de tuplas """
print("unionListToFormDictionari => ", unionListToFormDictionari)
""" ahora con lo anterior se forma el diccionario """
new_dict = {name:age for (name, age) in unionListToFormDictionari}
print("new_dict => ", new_dict)

print(" --------- Generacion de un diccionario pero con condicional -------------- ")
result = {country: population for (country, population) in population_2.items() if population < 800}
print("result => ", result)

print(" ----------Filtra las vocales------------- ")
text = "Hola soy Rigo"
mylist = list(text)
print("mylist => ", mylist)
unique = {caracter: caracter.upper() for caracter in text if caracter in 'aeiou'}
print("unique => ", unique)

