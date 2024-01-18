number = str(input('Anna kokonaisluku:'))
number2 = str(input('Anna toinen kokonaisluku:'))
number3 = str(input('Anna kolmas kokonaisluku:'))
my_list = [v for v in (number, number2, number3)]
print("Suurin:", max(my_list))