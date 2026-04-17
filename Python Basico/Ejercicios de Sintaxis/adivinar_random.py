import random

number_random = random.randint(1, 10)

number = int(input("Adivina el número entre 1 y 10: "))


while number != number_random:
    print("Número incorrecto. Intenta de nuevo.")
    number = int(input("Adivina el número entre 1 y 10: "))
    if number == number_random:
        print("Has adivinado el número.")
        break