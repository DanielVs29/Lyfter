list_a = ['first_name', 'last_name', 'role']
list_b = ['Daniel', 'Vargas', 'Software Engineer']

user_information = {}

for index in range(len(list_a)):
    user_information[list_a[index]] = list_b[index]

print(user_information)