def decimalToBinary(n):
    assert int(n) == n and 
    if n == 0:
        return 0
    return n % 2 + 10 * decimalToBinary(n // 2)

print(decimalToBinary(13))