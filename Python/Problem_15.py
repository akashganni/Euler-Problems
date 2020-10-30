from math import factorial
def ways(n):
    return (factorial(2*n)/(factorial(n) ** 2))

print(ways(20))
