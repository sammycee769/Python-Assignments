class Account:
    def __init__(self, pin):
        self.__pin = pin
        self.__balance = 0

    def validate_pin(self, pin):
        return self.__pin == pin

    def check_balance(self, pin):
        if self.validate_pin(pin):
            return self.__balance
        return "Invalid PIN"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount, pin):
        if self.validate_pin(pin):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                return self.__balance
        return "Invalid PIN or insufficient funds"
    
