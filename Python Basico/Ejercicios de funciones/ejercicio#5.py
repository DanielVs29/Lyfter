my_string = "I Love Nación Sushi"


def upper_and_lower_cases(string):
    upper_cases = 0
    lower_cases = 0

    for i in range(len(string)):
        if string[i].isupper():
            upper_cases += 1
        elif string[i].islower():   
            lower_cases += 1
            

    return upper_cases, lower_cases

print( "There are {} upper cases and {} lower cases.".format(upper_and_lower_cases(my_string)[0], upper_and_lower_cases(my_string)[1]) )