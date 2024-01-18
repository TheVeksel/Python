number = str(input('Anna kokonaisluku:'))
number2 = str(input('Anna toinen kokonaisluku:'))
my_list = [v for v in (number, number2)]
print("Pienempi:", min(my_list))