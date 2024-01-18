while True:
    sukunimi = input("Anna sukunimi: ")
    
    if not sukunimi:
        break
    
    with open('nimi.txt', 'a', encoding ="utf-8") as tiedosto:
        tiedosto.write(sukunimi + '\n')