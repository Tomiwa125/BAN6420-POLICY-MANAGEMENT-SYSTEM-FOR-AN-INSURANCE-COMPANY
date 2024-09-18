from Product import Product

class Payment:
    def __init__(self, policyholder, Product):
        self.policyholder = policyholder
        self.Product = Product
        self.amount_paid = 0

    def process_payment(self, amount):
        if amount >= self.product.premium:
            self.amount_paid += amount
            print(f"Payment of {amount} processed for {self.policyholder.name}.")
            return True
        else:
            print("Insufficient payment amount.")
            return False

    def send_reminder(self):
        print(f"Reminder: Payment due for {self.policyholder.name} on product {self.Product.name}.")

    def apply_penalty(self):
        penalty_amount = 50
        print(f"Penalty of {penalty_amount} applied to {self.policyholder.name}.")