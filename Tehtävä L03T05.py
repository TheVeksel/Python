def count_summa(getting_numbers):
    summa = 0
    for number in getting_numbers:
        if number > 0:
            summa += number
    return summa

users_numbers = []
for i in range(5):
    number = float(input(f"Anna luku {i+1}: "))
    users_numbers.append(int(number))

print("Annetut luvut:", users_numbers)

summa = count_summa(users_numbers)
print("Lukujen summa on:", int(summa))