def sum_of_fibonacci(num, first=1, second=2, su = 1):
    if second >= num:
        return su
    su += second
    new = first + second
    return sum_of_fibonacci(num, second, new, su)

print(sum_of_fibonacci(4000000))
