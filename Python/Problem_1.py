def is_multiple(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    return False

def sum(num):
    x = 1
    s = 0
    while x < num:
        if is_multiple(x) is True:
            s += x
        x += 1
    del x
    return s

print(sum(1000))
