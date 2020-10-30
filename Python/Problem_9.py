def pythagorean_triplet(num):
    a = 0
    while a < num:
        b = 0
        while b <  num:
            c = 0
            while c < num:
                if (a + b + c) == num and ((b ** 2) + (c ** 2) == (a ** 2)):
                    return (a*b*c), a, b, c
                c += 1
            b += 1
        a += 1


print(pythagorean_triplet(1000))
