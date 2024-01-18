def laske_nimet_tiedostosta(tiedostonimi):
    nimet = {}

    with open(tiedostonimi, 'r', encoding ="utf-8") as tiedosto:
        for nimi in tiedosto:
            nimi = nimi.strip()
            nimet[nimi] = nimet.get(nimi, 0) + 1

    return nimet

def tulosta_nimien_tilasto(nimet_tilasto):
    print("Nimiä löytyi yhteensä:", len(nimet_tilasto))
    print("Nimien esiintymiskerrat:")
    for nimi, kerrat in nimet_tilasto.items():
        print(f"{nimi}: {kerrat} kertaa")
        
tiedostonimi = 'nimet.txt'
nimet_tilasto = laske_nimet_tiedostosta(tiedostonimi)
tulosta_nimien_tilasto(nimet_tilasto)
