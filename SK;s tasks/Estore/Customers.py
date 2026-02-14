from Users import Users
from BillingInformation import BillingInformation
from  ShoppingCart import ShoppingCart

class Customers(Users):

    def __init__(self, name, home_address, age, email_address, password, phone_number):
        super().__init__(name, home_address, age, email_address, password, phone_number)
        self.billing_information: list[BillingInformation] = []
        self.cart = ShoppingCart()
