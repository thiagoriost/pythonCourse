from ecommerce.inventory_package.stock import get_stock

""" Agrega un producto al inventario """
def add_product(product_name, stock):
    get_stock()
    print(f'Producto {product_name} agregando con {stock} unidades.')
    
""" Elimina un pruducto del inventario """
def remove_product(produc_name):
    print(f'Producto {produc_name} elminando del inventario')