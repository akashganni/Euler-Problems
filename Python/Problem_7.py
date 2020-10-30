import math

def isprime(n):
    if(n+1) % 6 == 0 or (n-1) % 6 == 0:
        for i in range(2, int(round(math.sqrt(n)+1))):
            if n%i == 0:
                return False
        return True
    return False

def is_prime(num):
    x = 2
    while x < num:
        if num % x == 0:
            return False
        x += 1
    del x, num
    return True

def prime(num):
    n = 1
    x = 3
    while True:
        if isprime(x) is True:
            n += 1
        if n == num:
            del n, num
            return x
        x += 2

print(prime(10001))