def increment(x):
    return x+1

print(increment(5))
conLambda = lambda x: x+1
print(conLambda(15))

full_name = lambda name, lastName: f'{name.title()} {lastName.title()}'
print(full_name('rigo', 'rios'))
