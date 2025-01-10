
""" 
set_diferents_types_elements = {1, 'hola', False, 12.5}
print("set_diferents_types_elements => ", set_diferents_types_elements)

for e in set_diferents_types_elements:
    print("---- ",e)
    
set_from_string = set('hola')
print("set_from_string => ", set_from_string)

my_tupla = ('abc', 'asd', 'dfg', 'abc')
print("my_tupla => ", my_tupla)
set_from_tuples = set(my_tupla)
print("set_from_tuples => ", set_from_tuples)

my_list = [1,2,3,4,5,6,7,7]
print("my_list => ", my_list)
set_from_my_list = set(my_list)
print("set_from_my_list => ", set_from_my_list)

 """
 
""" Set's o conjuntos """
my_set_countries = {'col', 'mex', 'bol'}
print("my_set_countries => ", my_set_countries)
print(type(my_set_countries))
print("len => ", len(my_set_countries))
print("existe col", "col" in my_set_countries)
print("existe pe", "pe" in my_set_countries)
my_set_countries.add('pe')
print("existe pe", "pe" in my_set_countries)
# update a set
my_set_countries.update({'ar', 'ecu', 'pe'})
print("my_set_countries => ", my_set_countries)

# remove
my_set_countries.remove('col')
my_set_countries.discard('ar')
my_set_countries.discard('elemtoNoExiste') # con este no revienta el programa si no existe elemento
print("my_set_countries => ", my_set_countries)
# limpiar el conjunto
my_set_countries.clear()
print("my_set_countries => ", my_set_countries)
