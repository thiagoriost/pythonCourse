def print_info(**kwargs): # llega un diccionario
    print("kwargs => ", kwargs)
    """ for key, value in kwargs.items():
        print(f'{key}: {value}') """
        
    for k,v in kwargs.items():
        print("dato => ", k, v)
        print(f'{k}: {v}')

print_info(name='Carlos', age=30, city='Bogotá') # argumentos posicionales
print_info(name='Carlos', age=30, city='Bogotá', country = 'Colombia')