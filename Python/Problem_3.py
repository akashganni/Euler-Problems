def largest_prime(num):
    x = 2
    while x < num:
        if num % x == 0:
            num = num / x
            x = 1
        x += 1
    return num


print(largest_prime(600851475143))
