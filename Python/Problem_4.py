def largest(digit):
    p = int(10**len(str(digit)))
    n = 0
    s = None
    a = digit
    b = digit
    while n < p:
        x  = 0
        b = digit
        while x < p:
            res = a * b
            if s == None or res > s:
                if palindrome(res) is True:
                    s = res
                    q = (a, b)
            b -= 1
            x += 1
        a -= 1
        n += 1
    if s == None:
        return largest(digit-p)
    return s, q


def palindrome(num):
    num = list(str(num))
    x = num.copy()
    num.reverse()
    if x == num:
        del x, num
        return True
    del x, num
    return False

def main(num):
    num = (10**num) - 1
    print(largest(num))

main(2)