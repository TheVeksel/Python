class BankAccount:
    def __init__(self, perus_saldo = 2000):
        self.saldo = perus_saldo

    def lisa(self, raha):
        self.saldo += raha
        print(f"Bank account balance: {self.saldo}€")

    def nostaa(self, raha):
        if raha > 0 and raha <= self.saldo:
            self.saldo -= raha
            print(f"Bank account balance: {self.saldo}€")
        else:
            print(f"Sorry, you have only {self.saldo}€, the withdraw cannot be done.")

pankkitili = BankAccount()

print("Bank account created.")
print(f"Bank account balance: {pankkitili.saldo}€")

lisraha = int(input("How many euros will be added? "))
pankkitili.lisa(lisraha)

nostaaraha = int(input("How many euros will be withdrawn? "))
pankkitili.nostaa(nostaaraha)

nostaaraha2 = int(input("How many euros will be withdrawn? "))
pankkitili.nostaa(nostaaraha2)
