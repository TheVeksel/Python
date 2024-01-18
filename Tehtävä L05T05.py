def get_cost(num1, num2, num3):
    a = (num2 * num1 / 100) * num3
    ra = round(a, 2)
    return ra

print(get_cost(100,7.5,1.88))
print(get_cost(220,6.9,1.88))