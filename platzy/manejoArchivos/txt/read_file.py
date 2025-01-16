import os
# print("/////////////")
# print(os.getcwd())  # Muestra el directorio actual
# print("/////////////")

path = os.getcwd()+r"\platzy\manejoArchivos\cuento.txt"
path_textoPrueba = os.getcwd()+r"\platzy\manejoArchivos\txt\textoPrueba.txt"
print("path_textoPrueba => ", path_textoPrueba)

file = open(path_textoPrueba)
# print("file => ", file.read())
# print( file.readline())
# print( file.readline())
print( file.readlines())

file.close()

# lee archivo linea a linea y cuando termina lo cierra
# con r+ permite leer y escribir
# con w+ permite leer y sobreescribir
"""with open(path, 'r+') as file:
    for lineas in file:
        print(lineas.strip())"""
        
# leer todas las lineas en una lista
""" with open(path, 'r') as file:
    lineas = file.readlines()
    print(lineas)
    print(len(lineas))
 """    
# escribir en el archivo, addicionando al final una fila de texto
# with open(path, 'a') as file:
#     file.write("\n\nFixed By RigoRios")
    
# sobreescribir el texto
# with open(path, 'w') as file:
#     file.write("\n\nFixed By RigoRios and chatGPT")

