from datetime import datetime

current_year = datetime.now().year

users_birthdate = int(input('Mikä on sun syntymävuosi? '))

age1 = current_year - users_birthdate

def kerro3(age):
    if age <= 1:
        return(f'{age} - baby')
    elif age <= 13:
        return(f'{age} - child')
    elif age == 13 or age <= 19:
        return(f'{age} - teen')
    elif age == 20 or age <= 65:
        return(f'{age} - adult')
    else:
        return(f'{age} - senior')

print(kerro3(age1))