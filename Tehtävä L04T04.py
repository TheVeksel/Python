getnumber = int(input("Anna numero väliltä 1-10: "))
if 1 <= getnumber <= 10:
    for i in range(1, getnumber + 1):
        neliö = i ** 2
        print(f"Luvun {i} neliö on {neliö}")
else:
    print("Anna luku väliltä 1-10.")