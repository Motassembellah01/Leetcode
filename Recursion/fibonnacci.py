# f(n) = f(n - 1) + f(n - 2)

def fibonacci(n):
    assert n >= 0 and int(n) == n, 'The fibonnacci function must take a positive integer'
    if n in [0, 1]:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 
