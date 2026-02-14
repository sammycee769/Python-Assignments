from abc import ABC

class Users(ABC):

    def __init__(self, name, age,home_address, email_address, password, phone_number):
        self.name = name
        self.age = age
        self.email_address = email_address
        self._password = password
        self.phone_number = phone_number
        self.home_address = home_address


