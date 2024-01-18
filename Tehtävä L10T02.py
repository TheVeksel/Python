ask = int(input('Insert year: '))

if  (ask % 4 == 0 and ask % 100 != 0) or (ask % 400 == 0):
    print(f'{ask} is a leap year')
else:
    print(f'{ask} is not a leap year')
