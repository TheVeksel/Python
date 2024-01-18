try:
    with open('C:/ayho.txt', 'w', encoding ="utf-8") as file:
        file.write("Toivon, että se toimii.")

except PermissionError:
    print("Ei oikeuksia kirjoittaa tiedostoon.")
except Exception as e:
    print(f"Jotain virhe tapahtui: {e}")
