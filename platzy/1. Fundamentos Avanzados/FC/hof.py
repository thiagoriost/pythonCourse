""" 
HOF => Hide Order Funtion
"""

hof = lambda x, func : x + func(x)

response = hof(5, lambda x : x+1)

print(response)