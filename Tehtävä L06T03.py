oppilaat = []

while True:
    names = input("Anna oppilaan nimi: ")
    
    if not names:
        break
    
    oppilaat.append(names)

print(f"Oppilaita: {len(oppilaat)}")
print(", ".join(oppilaat))
