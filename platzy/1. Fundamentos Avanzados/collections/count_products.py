from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    #Crea un diccionario con valor por defecto 0 
    product_count = defaultdict(int)
    print("product_count => ",product_count)
    for product in orders:
        product_count[product] +=1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)
