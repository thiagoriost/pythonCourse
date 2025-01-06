import math, random

#hallar el area y perimetro de un circulo
radius = 5
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius
print(area)
print(perimeter)

print("//////// random ///////////")
random_number = random.randint(1, 10)

# Elegir colores aleatorios
colors = ['red', 'blue', 'green']
random_color = random.choice(colors)
print("random_color => ", random_color)

print("//////// Barajar lista de cartas ///////////")
cards = ['As', 'King', 'Queen', 'Jota', '10']
random.shuffle(cards)
print("cards => ", cards)