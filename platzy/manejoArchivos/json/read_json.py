import json, os

def show_products(products):
    # Mostrar contenido
    for product in products:
        # print(product)
        print(f"Product: {product['name']}, Price:{product['price']}")    

# referencia el arcivo a explorar
fileOriginal = os.getcwd()+r"\platzy\manejoArchivos\json\products.json"
# abre el archivo
with open(fileOriginal, mode='r') as jsonFile:
    products = json.load(jsonFile)
    
show_products(products)
    
newProduct = {
      "name": "Laptop",
      "price": 1200,
      "quantity": 4,
      "brand": "BrandName",
      "category": "Electronics",
      "entry_date": "2024-01-05"
    }

products.append(newProduct)
print("///////////////////")
show_products(products)
# modificar json con la nueva adicion
with open(fileOriginal, mode='w') as w_jsonFile:
    json.dump(products, w_jsonFile, indent=4)