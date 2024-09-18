from Payment import Payment
from Policyholder import Policyholder
from Product import Product


def main():
    # Create products
    health_insurance = Product("Health Insurance", 500)
    health_insurance.create()

    life_insurance = Product("Life Insurance", 500)
    life_insurance.create()

    # Create policyholders
    timothy_doe = Policyholder("Timothy doe", "tommyadubi1@gmail.com")
    timothy_doe.register()

    julius_wrecker = Policyholder("Julius Wrecker", "julius@gmail.com")
    julius_wrecker.register()

    # Add products to policyholders
    timothy_doe.add_product(health_insurance)
    julius_wrecker.add_product(life_insurance)

    # Process payments
    timothy_payment = Payment(timothy_doe, health_insurance)
    timothy_payment.process_payment(300)

    julius_payment = Payment(julius_wrecker, life_insurance)
    julius_payment.process_payment(500)

    # Display account details
    timothy_doe.display_account_details()
    julius_wrecker.display_account_details()

if __name__ == "__main__":
    main()