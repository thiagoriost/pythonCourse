import csv, os
# import os


# leer un archivo
# E:\software\PYTHON\platzy\manejoArchivos\csv\products.csv
path = os.getcwd()+"\platzy\manejoArchivos\csv\products.csv"
with open(path, mode='r') as file:
    csv_reader = csv.DictReader(file) #abrir el csv en formato de diccionario
    for row in csv_reader:
        print(row)

# Mostrar info por columnas
with open(path, mode='r') as file:
    csv_reader = csv.DictReader(file) #abrir el csv en formato de diccionario
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")