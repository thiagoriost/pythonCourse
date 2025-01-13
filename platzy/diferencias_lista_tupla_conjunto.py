""" 
        Mutable     Ordenada    indexing/Slicing    Duplicar_elementos
List    ok          ok          ok                  ok
Tuple   x           ok          ok                  ok
Set     ok          x           x                   x
"""

price = 100

def incre():
    price_1 = price +  10
    print(price_1)
    
incre()
print(price)
