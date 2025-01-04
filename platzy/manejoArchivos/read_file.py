import os
# print("/////////////")
# print(os.getcwd())  # Muestra el directorio actual
# print("/////////////")

path = os.getcwd()+"\platzy\manejoArchivos\cuento.txt"
# print("path => ", path)
# lee archivo linea a linea
"""with open(path, 'r') as file:
    for lineas in file:
        print(lineas.strip())"""
        
# leer todas las lineas en una lista
# with open(path, 'r') as file:
#     lineas = file.readlines()
#     print(lineas)
    
# escribir en el archivo, addicionando al final una fila de texto
# with open(path, 'a') as file:
#     file.write("\n\nFixed By RigoRios")
    
# sobreescribir el texto
with open(path, 'w') as file:
    file.write("\n\nFixed By RigoRios and chatGPT")