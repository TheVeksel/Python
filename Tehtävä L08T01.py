names = []
for i in range(10):
    nimi = input(f"Anna 10 kavereiden nimet: ")
    names.append(nimi)

print("Kaverit:")
for nimi in names:
    print(nimi)

print("Kaverit:")
for nimi in reversed(names):
    print(nimi)
