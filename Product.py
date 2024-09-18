class Product:
    def __init__(self, name, premium):
        self.name = name
        self.premium = premium
        self.active = True

    def create(self):
        print(f"Product {self.name} created with premium {self.premium}.")

    def update(self, new_premium):
        self.premium = new_premium
        print(f"Product {self.name} updated to premium {new_premium}.")

    def suspend(self):
        self.active = False
        print(f"Product {self.name} has been suspended.")
