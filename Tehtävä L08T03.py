arvosanat = []

while True:
    arvosana_str = input('Anna arvosana: ')

    if not arvosana_str.strip():
        break

    try:
        arvosana = int(arvosana_str)

        if 0 <= arvosana <= 5:
            arvosanat.append(arvosana)
        else:
            print('Arvosanan tulee olla välillä 0-5.')
    except ValueError:
        print('Virheellinen syöte. Anna kokonaisluku arvosanaksi.')

if arvosanat:
    keskiarvo = sum(arvosanat) / len(arvosanat)
    print(f'Annoit {len(arvosanat)} arvosanaa')
    print(f'Keskiarvo: {round(keskiarvo, 1)}')
