a=2
b=3
c=a+b
print(c)

# concatenar
nombre = " Rigo "
mensaje = f"Hola {nombre}, esto es un f string"
print(mensaje)

# operadores de pertenencia (in / not in)
print("Rigo" in mensaje) #retorna un boolean
print("Rigo" not in mensaje) #retorna un boolean

# con del se puede borrar una variable
del mensaje
print(mensaje)
