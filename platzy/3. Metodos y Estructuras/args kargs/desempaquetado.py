#Desempaquetado args
def add(a, b, c):
    return a + b + c

values = (1, 2, 3)
print("values => ", values)
print("*values => ", *values)
print(add(*values)) 

def show_info(name, age):
    print("name =>", name)
    print("age =>", age)
    print(f"Name: {name}, Age: {age}")

data = {"name": "Ana", "age": 28}
print("data => ", data)

show_info(**data)