def isPrime(num):
    x = 2
    s = 0
    while x <= num:
        if num % x == 0:
            num = num / x
            x = 1
            s += 1
        x += 1
    return s

def sumPrimes(num):
    x = 3
    s = 2
    while x < num:
        if isPrime(x) == 1:
            s += x
        x += 2
    return s

print(sumPrimes(10))