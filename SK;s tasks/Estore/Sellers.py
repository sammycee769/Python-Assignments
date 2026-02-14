from Users import Users

class Sellers(Users):

    def __init__(self, name, home_address, age, email_address, password, phone_number):
        super().__init__(name, home_address, age, email_address, password, phone_number)
        