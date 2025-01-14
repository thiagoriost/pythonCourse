numbers = list(range(1,5))
print(numbers)

result = [i*2 for i in numbers]
print(result)

result_1 = list(map(lambda i:i*2, numbers))
print(result_1)

print("-"*20)

numbers_1 = list(range(1,5))
print(numbers_1)
numbers_2 = list(range(5,8))
print(numbers_2)

result_2 = list(map(lambda x, y:x+y, numbers_1, numbers_2))
print(result_2)
