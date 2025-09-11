def gcd(a, b):
    assert int(a) == a and int(b) == b, 'Numbers must be integer'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b

    elif b == 0:
        return a

    return gcd(b, a%b)


print(9327 % 24)

