my_list = [4, 3, 6, 1, 7]

new_list = []
first = None

for index, record in enumerate(my_list):
    if index == 0:
        first = record
    elif index == len(my_list) - 1:
        new_list.insert(0, record)
        new_list.append(first)
    else:
        new_list.append(record)

my_list = new_list

print(my_list)
