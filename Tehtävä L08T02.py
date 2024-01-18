rekisterinumerot = []

while True:
    rekisterinumero = input("Syötä rekisterinumero: ")
    
    if not rekisterinumero:
        break
    
    rekisterinumerot.append(rekisterinumero)

rekisterinumerot.sort()
print("\nSyötyt rekisterinumerot aakkosjärjestyksessä:")
for numero in rekisterinumerot:
    print(numero)
