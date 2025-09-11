# 3456789

def sumDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be an integer positive'

    extractingNumber = n // (10**(len(str(n)) - 1))

    if n == 0:
        return n
    
    else:
        return extractingNumber + sumDigits(n % (10**(len(str(n)) - 1))) 


print(sumDigits(3456789))


# Another way to do so

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be an integer positive'
    if n == 0:
        return n
    
    else:
        return n % 10 + sumOfDigits(n // 10)

    

