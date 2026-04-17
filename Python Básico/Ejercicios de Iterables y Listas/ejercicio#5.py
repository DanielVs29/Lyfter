user_list = []
top = 0

for i in range(0,10,1):
    number = int(input(f"ingrese el numero {i+1}: "))
    user_list.append(number)

for i, value in enumerate(user_list):
    if user_list[i]> top:
        top = user_list[i]


print(f"la lista de numeros ingresados es: {user_list}. El numero mas alto :{top}.")
