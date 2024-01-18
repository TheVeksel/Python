class Cat:
    def __init__(self, color):
        self.color = color

    def miau(self):
        return "Meooooow!"

kit = Cat(color="black")
kat = Cat(color="white")

print(f"Kit, color: {kit.color}")
print(f"Kat, color: {kat.color}")

print(f"Kit says: {kit.miau()}")
print(f"Kat says: {kat.miau()}")
