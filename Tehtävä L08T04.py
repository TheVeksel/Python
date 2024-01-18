autot = {
    'ABC-123': 'Skoda',
    'XYZ-789': 'Toyota',
    'DEF-456': 'Ford',
    'GHI-789': 'Honda',
    'JKL-012': 'Chevrolet',
    'MNO-345': 'Volkswagen',
    'PQR-678': 'Nissan',
    'STU-901': 'Hyundai',
    'VWX-234': 'Mazda',
    'YZA-567': 'Kia'
}

print("Autot:")
for rekisterinumero, merkki in autot.items():
    print(f"Rekisterinumero: {rekisterinumero}, Merkki: {merkki}")

print("\nAutot aakkosjärjestyksessä:")
sorted_autot = sorted(autot.items(), key=lambda x: x[0])
for rekisterinumero, merkki in sorted_autot:
    print(f"Rekisterinumero: {rekisterinumero}, Merkki: {merkki}")
