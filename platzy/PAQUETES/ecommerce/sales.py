# from sales_package.orders import get_order
from ecommerce.sales_package.orders import get_order

def process_sale(product_name, quantity):
    get_order()
    print(f'Venta procesada: {quantity}, unidades de {product_name}')
