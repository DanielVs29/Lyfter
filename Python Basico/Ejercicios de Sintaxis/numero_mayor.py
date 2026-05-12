number1 = int(input("Introduce el primer número: "))
number2 = int(input("Introduce el segundo número: "))
number3 = int(input("Introduce el tercer número: ")) 

if number1 >= number2 and number1 >= number3:
    top = number1
elif number2 >= number1 and number2 >= number3:
    top = number2
else:
    top = number3

print(f"El número mayor es: {top}")