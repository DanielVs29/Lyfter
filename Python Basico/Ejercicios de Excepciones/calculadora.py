def main():
    
    while True:
        try:
            number = int(input("Ingrese el primer numero: \n"))
            break
        except ValueError:
            print("Debe ingresar un número válido")

    try:
        calculate(number)
    except Exception as ex:
        print ( f'Ocurrio un error: { ex } ' )


def sum_numbers(num1, num2):
    return num1 + num2
    

def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    return num1 / num2


def read_number(number):
    while True:
        try:
            return int(input(number))
        except ValueError:
            print("Debe ingresar un número válido")


def calculate(number):
    
    while True:

        try:
            opcion = int(input("Seleccione una opcion:\n\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Borrar resultado\n"))
        except ValueError:
            print("Opción inválida")
            continue

        if opcion == 1:
            number2 = read_number("Ingrese numero a sumar: ")
            number = sum_numbers(number, number2)
            print("Resultado:", number)

        elif opcion == 2:
            number2 = read_number("Ingrese numero a restar: ")
            number = subtract_numbers(number, number2)
            print("Resultado:", number)

        elif opcion == 3:
            number2 = read_number("Ingrese numero a multiplicar: ")
            number = multiply_numbers(number, number2)
            print("Resultado:", number)

        elif opcion == 4:
            number2 = read_number("Ingrese numero a dividir: ")
            
            if number2 == 0:
                print("No se puede dividir entre 0")
            else:
                number = divide_numbers(number, number2)
                print("Resultado:", number)

        elif opcion == 5:
            number = 0
            print("Se ha eliminado el resultado correctamente")

        else:
            print("\nOpción inválida")


if __name__ == "__main__":
    main()