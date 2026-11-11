import random
import time

secreto = random.randint(1, 100)
intentos = 0

print("Bienvenido al juego de adivinar el número!   ")
time.sleep(1)
print("Estoy pensando en un número entre 1 y 100. Intenta adivinarlo.")
while True:

    try:
        guess = int(input("Ingresa el numero: "))
    except ValueError:
        print("Por favor ingresa un numero valido.")
        continue

    intentos += 1

    if guess < secreto:
        print("El numero es mayor")
    elif guess > secreto:
        print("El numero es menor")
    else:
        print(f"Felecitaciones! Adivinaste el numero en {intentos} intentos.")