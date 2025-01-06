import csv, os, random

fileOriginal = os.getcwd()+r"\platzy\manejoArchivos\csv\products.csv"
fileUpdate = os.getcwd()+r"\platzy\manejoArchivos\csv\products_updated.csv"
with open(fileOriginal, mode='r') as file: # abre el archivo en modo lectura
    # file.write('\n') # agrega un salto de linea al archivo a editar
    csv_reader = csv.DictReader(file) # formatea en modo de diccionario
    # Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames # obtiene el nombre de las columnas
    print(fieldnames)
    newColumns = ['total_value', 'columnaReto1', 'columnaReto2'] # nombre de la nueva columna
    for nc in newColumns:
        print(nc)
        fieldnames = fieldnames + [nc] # agrega la nueva columna
    print(fieldnames)
    with open(fileUpdate, mode='w', newline='') as fileUpdate: # referencia la ubicacion del nuevo archivo
        csv_writer = csv.DictWriter(fileUpdate, fieldnames=fieldnames) # set nuevas columnas
        print("csv_writer")
        print(csv_writer)
        print("///////////////")
        csv_writer.writeheader() # escribir encabezados
        for row in csv_reader: # recorre las filas del file original y guarda en el archivo nuevo con los ajustes
            for nw in newColumns:
                if nw == 'total_value':
                    row[nw] = float(row['price']) * int(row['quantity'])# agrega la nueva columna para cada fila con su respectivo valor
                else:
                    row[nw] = random.randint(100, 1000)  # agrega la nueva columna para cada fila con su respectivo valor
            csv_writer.writerow(row)