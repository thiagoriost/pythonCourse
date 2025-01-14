items = [
    {
        'product':'camisa',
        'price':100
    },
    {
        'product':'pantalones',
        'price':300
    },
    {
        'product':'Saco',
        'price':200
    }
]
print("items => ", items)

""" obtener solo los precios """
prices = list(map(lambda e : e['price'], items))
print("prices => ", prices)

def add_taxes(item): 
    clone_item = item.copy()
    clone_item['tax'] = clone_item['price'] * .19
    return clone_item

new_items = list(map(add_taxes, items))
print("new_items => ", new_items)
print("items => ", items)

print("-"*20)

def multiply_numbers(numbers):
    return list(map(lambda e : e*2, numbers))

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)
