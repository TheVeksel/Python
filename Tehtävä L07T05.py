class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car(brand="Skoda", model="Octavia", price=3000)
car2 = Car(brand="Audi", model="A4", price=4000)
car3 = Car(brand="Volvo", model="V70", price=5000)

print(f"Auto 1: {car1.brand} {car1.model}, Hinta: ${car1.price}")
print(f"Auto 2: {car2.brand} {car2.model}, Hinta: ${car2.price}")
print(f"Auto 3: {car3.brand} {car3.model}, Hinta: ${car3.price}")

yhteishinta = car1.price + car2.price + car3.price
print(f"Autojen hinta yhteensä: ${yhteishinta}")
