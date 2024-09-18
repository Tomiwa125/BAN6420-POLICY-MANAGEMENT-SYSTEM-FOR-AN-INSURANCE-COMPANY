class Policyholder:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.active = True
        self.products = []

    def register(self):
        print(f"{self.name} has been registered.")

    def suspend(self):
        self.active = False
        print(f"{self.name} has been suspended.")

    def reactivate(self):
        self.active = True
        print(f"{self.name} has been reactivated.")

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added to {self.name}'s account.")

    def display_account_details(self):
        status = "Active" if self.active else "Suspended"
        product_names = [product.name for product in self.products]
        print(f"Policyholder: {self.name}, Email: {self.email}, Status: {status}, Products: {product_names}")