import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("¿Cuántos caracteres tendrá la contraseña? "))

contraseña = ''

for i in range(longitud):
    contraseña += random.choice(caracteres)
    
print(contraseña)

