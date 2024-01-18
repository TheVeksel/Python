count = True
count1 = 0
summa = 0

while count:
    try:
        number = int(input('Anna luku: '))
        count1 += 1
        summa += number
    except:
        print('Lukuja annettu: ' + str(count1))
        print('Lukujen summa: ' + str(summa))
        count = False