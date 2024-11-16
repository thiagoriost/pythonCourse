# lista
myLista = ["texto", "rigo", True, 1.85, 5]
print(myLista)
print(myLista[0])
myLista[0]=55
print(myLista)


#tuplas, estas no se pueden modificar
myTupla = ("texto", "rigo", True, 1.85, 5)
print(myTupla)
print(myTupla[1])

# set solo se puede reescribir toda la varibale de tipo set, mas no se puede 
# modificar alguno de sus elementos, los elementos se leen de forma aleatoria o desordenada
# no se puede acceder a ningun elemente de forma individual, elimina elemento repetidos
# solo por medio de un bucle se puede acceder a cada elemento
mySet = {"texto", "rigo", True, 1.85, 5, 5}
print(mySet)
mySet = {"1", "2", True, 1.85, 5, 5}
print(mySet)

#Diccionario, es como json de javaScript
myDiccionario = {
    'nombre': 'Rigo',
    'edad'   : 15,
    'dir': 'Villa',
    'single': True,
    'testDuplicado': 'Villa'
}
print(myDiccionario)
print(myDiccionario['nombre'], myDiccionario['single'])
