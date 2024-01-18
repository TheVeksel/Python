def get_fuel(num1,num2):
    a = num2 * num1 / 100
    ra = round(a, 1)
    return ra

print(get_fuel(100,7.5))
print(get_fuel(220,6.9))