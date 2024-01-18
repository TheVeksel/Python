class adam:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

pers1 = adam("Adam", "19")

print(pers1)

class eva:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

pers2 = eva("Eva", "18")

print(pers2)
