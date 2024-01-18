try:
    with open('names.txt', 'r') as file:
        lines = file.readlines()

        number_of_names = len(lines)
        print(f"Nimiä löytyi: {number_of_names}")

        shortest_name = min(lines, key=lambda x: len(x.strip()))
        print(f"Pisin nimi on: {shortest_name.strip()}")

except FileNotFoundError:
    print("Tiedostoa names.txt ei löytynyt.")
except Exception as e:
    print(f"Jotain virhe tapahtui: {e}")
