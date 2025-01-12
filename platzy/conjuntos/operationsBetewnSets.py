set_a = {'col','mex','bol'}
set_b = {'pe','bol'}
print("set_a => ", set_a)
print("set_b => ", set_b)

# union entre 2 conjunto, existen 2 maneras, acontinuación
print("union entre 2 conjunto")
set_c_0 = set_a.union(set_b)
set_c_1 = set_a | set_b
print("set_c_0 => ", set_c_0)
print("set_c_1 => ", set_c_1)

# Interseccion entre 2 conjunto, existen 2 maneras, acontinuación
print("Interseccion entre 2 conjunto")
set_c_0 = set_a.intersection(set_b)
set_c_1 = set_a & set_b
print("set_c_0 => ", set_c_0)
print("set_c_1 => ", set_c_1)

# Diferencia entre 2 conjunto, existen 2 maneras, acontinuación
print("Diferencia entre 2 conjunto")
set_c_0 = set_a.difference(set_b)
set_c_1 = set_a - set_b
print("set_c_0 => ", set_c_0)
print("set_c_1 => ", set_c_1)

# Diferencia simetria entre 2 conjunto, existen 2 maneras, acontinuación
print("Diferencia simetria entre 2 conjunto")
set_c_0 = set_a.symmetric_difference(set_b)
set_c_1 = set_a ^ set_b
print("set_c_0 => ", set_c_0)
print("set_c_1 => ", set_c_1)


countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set = countries | northAm | centralAm | southAm

print(new_set)