luvut = []
while True:
    syote = input('Anna luku: ')
    if not syote:
        with open('luvut.txt', 'w', encoding ="utf-8") as file:
            for luku in luvut:
                file.write(str(luku) + '\n')
        print(f'Kiitos')
        break
    luku = int(syote)
    luvut.append(luku)

print(f'Syötetty {len(luvut)} lukua.')
