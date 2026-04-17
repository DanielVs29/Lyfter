user_name = input("Ingrese su nombre: ")
user_last_name = input("Ingrese su apellido: ")
user_age = int(input("Ingrese su edad: "))  

if user_age <= 2:
    print(f"{user_name} {user_last_name}, eres un bebé.")

elif user_age > 2 and user_age <= 9:
    print(f"{user_name} {user_last_name}, eres un niño.")

elif user_age >= 10 and user_age <= 12:
    print(f"{user_name} {user_last_name}, eres un preadolescente.")

elif user_age >= 13 and user_age <= 17:
    print(f"{user_name} {user_last_name}, eres un adolescente.")

elif user_age >= 18 and user_age <= 29:
    print(f"{user_name} {user_last_name}, eres adulto joven.")

elif user_age >= 30 and user_age <= 59:
    print(f"{user_name} {user_last_name}, eres adulto.")

elif user_age >= 60:
    print(f"{user_name} {user_last_name}, eres adulto mayor.")
