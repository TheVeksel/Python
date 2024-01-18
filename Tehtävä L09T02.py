with open('nimi.txt', 'r', encoding='utf-8') as file:
    nimet = [line.strip() for line in file]

print("Nimet alkuperäisessä järjestyksessä:")
for nimi in nimet:
    print(nimi)

nimet = sorted(nimet, key=str.lower)

print("\nNimet aakkosjärjestyksessä:")
for nimi in nimet:
    print(nimi)
