def power(base, expo):
    assert int(expo) == expo,'Expo must be integer'
    if expo == 0:
        return 1

    elif expo < 0:
        return 1/base * power(base, expo+1)

    return base * power(base, expo - 1)


print(power(4, -1))