class Pelikortti:
    def __init__(self, maa, arvo):
        self.maa = maa
        self.arvo = arvo

korttiy = Pelikortti(maa="ruutu", arvo=3)
korttikaks = Pelikortti(maa="risti", arvo=5)
korttiko = Pelikortti(maa="pata", arvo=14)
korttine = Pelikortti(maa="risti", arvo=9)
korttiviis = Pelikortti(maa="hertta", arvo=2)

print(f"Kortti 1: {korttiy.maa}, {korttiy.arvo}")
print(f"Kortti 2: {korttikaks.maa}, {korttikaks.arvo}")
print(f"Kortti 3: {korttiko.maa}, {korttiko.arvo}")
print(f"Kortti 4: {korttine.maa}, {korttine.arvo}")
print(f"Kortti 5: {korttiviis.maa}, {korttiviis.arvo}")
