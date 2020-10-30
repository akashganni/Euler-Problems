def sum_of_squares(num):
    x = 1
    s = 0
    while x <= num:
        s += (x**2)
        x += 1
    del num, x
    return s

def sqare_of_sum(num):
    x = 1
    s = 0
    while x <= num:
        s += x
        x += 1
    del num, x
    return (s**2)

def main(num):
    print(sqare_of_sum(num) - sum_of_squares(num))

main(100)