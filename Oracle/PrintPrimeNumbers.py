
def is_prime(number):

    if number == 0 or number == 1:
        return False

    for x in range(2,number):
        if x != number and number % x == 0:
            return False

    return True

def print_primes(to_number):

    for x in range(to_number + 1):
        if is_prime(x):
            print(str(x))

print_primes(10)


