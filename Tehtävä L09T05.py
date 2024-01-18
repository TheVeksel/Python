import random

def arvo_lottorivi():
    return random.sample(range(1, 41), 7)

def tallenna_lottorivit(tiedostonimi, kysymys):
    with open(tiedostonimi, 'w', encoding ="utf-8") as file:
        for _ in range(kysymys):
            lottorivi = arvo_lottorivi()
            file.write(' '.join(map(str, lottorivi)) + '\n')

filename = 'lotto.txt'
kysymys = int(input('Montako lottoriviä arvotaan? '))

tallenna_lottorivit(filename, kysymys)
print(f'Lottorivit tallennettu tiedostoon "{filename}".')