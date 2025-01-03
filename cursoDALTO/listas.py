rango = range(1,11)
print("rango => ", rango)
squares = [x**2 for x in rango]
print("Cuadrados: ", squares)

celsius = [0, 10, 20, 30, 40]
farenheith = [(temp * 9/5) * 32 for temp in celsius]
print("farenheith => ", farenheith)

dato = [1, 2, 3, 4, 5]
result = [d + 1 for d in dato]
print("result => ", result)

print("######### Numeros pares ################")
evens = [x for x in range(1,21) if x%2 == 0]
print("evens => ", evens)

print("######### Transpuesta de una matriz ################")
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print("matrix => ", matrix)

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("transposed => ", transposed)




