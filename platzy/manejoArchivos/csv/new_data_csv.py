import csv, os


new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2025-01-04',
}
path = os.getcwd()+"\platzy\manejoArchivos\csv\products.csv"
with open(path, mode='a', newline='') as file:
    file.write('\n') # agrega un salto de linea al archivo a editar
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)