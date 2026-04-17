my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11,11, 12]

par_list = []

for value in my_list:
    if value % 2 == 0:
        par_list.append(value)

print(par_list)