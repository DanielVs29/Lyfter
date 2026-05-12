my_list = [1, 4, 6, 7, 13, 9, 67]

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def get_primes(list_of_numbers):

    primes = []

    for num in list_of_numbers:
        if is_prime(num):
            primes.append(num)

    return primes

print(get_primes(my_list))