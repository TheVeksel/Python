def celToFah(num1):
    a = num1
    ra = a * 9 / 5 + 32
    return ra

print(celToFah(10.0))


def fahToCel(num2):
    b = num2
    ba = (b - 32) * 5 / 9
    baa = round(ba, 1)
    return baa

print(fahToCel(38.0))	