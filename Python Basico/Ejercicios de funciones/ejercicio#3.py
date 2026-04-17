list = [4, 6, 2, 29]

def sum_list(list):
    sum = 0
    
    for i in list:
        sum += i
    return sum

print(sum_list(list))