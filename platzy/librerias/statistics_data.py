import statistics, csv, os

# Leer los datos de ventas mensuales desde un archivo CSV
fileToRead = os.getcwd()+r"\platzy\librerias\monthly_sales.csv"
monthly_sales = {}
with open(fileToRead, mode='r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print("sales => ", sales)

# Hallas la maximoVentas
maximoVentas = max(sales)
print("La maximoVentas es: ", maximoVentas)

# Hallas la minVentas
minVentas = min(sales)
print("La minVentas es: ", minVentas)

# Hallas la media
media = statistics.mean(sales)
print("La media es: ", media)

# Hallas la mediana
mediana = statistics.median(sales)
print("La mediana es: ", mediana)

# Hallas la moda
moda = statistics.mode(sales)
print("La moda es: ", moda)

# Hallas la desviacionEstandar
desviacionEstandar = statistics.stdev(sales)
print("La desviacionEstandar es: ", desviacionEstandar)

# Hallas la varianza
varianza = statistics.variance(sales)
print("La varianza es: ", varianza)