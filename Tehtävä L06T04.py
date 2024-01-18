a = []

while len(a) != 5:
    pist = int(input('Hypyn pisteet: '))
    a.append(pist)
    if len(a) == 5:
        a.sort()
        del a[0]
        del a[-1]
        print(sum(a))
        break
