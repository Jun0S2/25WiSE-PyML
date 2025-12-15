from operator import mod

def divides(num, div):
    return num % div == 0


def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if divides(num, i):
                break
        else:
            primes.append(num)
    return primes


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if divides(num, 2) or divides(num, 3):
        return False
    i = 5
    while i * i <= num:
        if divides(num, i) or divides(num, i + 2):
            return False
        i += 6
    return True


def find_primes_faster(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes
