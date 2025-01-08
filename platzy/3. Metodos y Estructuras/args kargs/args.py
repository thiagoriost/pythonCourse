

def sum_numbers(*args): # * cuando no se tiene certeza de parámetros, la variable args es una tupla la cual no se modifica
    print("args => ", args)
    print(" -------------------------- ")
    return sum(args)

print(sum_numbers(1,2,3,4,5))
print(sum_numbers(1,2))
print(sum_numbers(1,2,3,4,5,7,8,9,10,1))