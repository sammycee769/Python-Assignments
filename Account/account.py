class Account:
    def __init__(self, pin, name, phone_number):
        self.balance = 0
        self.pin = self._validate_pin(pin)
        self._validate_name(name)
        self.name = name
        self._verify_phone_number(phone_number)
        self.phone_number = phone_number
        self.account_number = None

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_number(self):
        return self.account_number

    def _verify_pin(self, pin):
        if self.pin != pin:
            raise ValueError("Invalid pin")

    def _verify_phone_number(self, phone_number):
        phone_number = phone_number.strip()

        if phone_number == "":
            raise ValueError("Phone number cannot be empty")

        if len(phone_number) != 11:
            raise ValueError("Phone number must be 11 characters long")

        if not phone_number.isdigit():
            raise ValueError("Phone number must contain only digits")

        if not phone_number.startswith("0"):
            raise ValueError("Phone number must start with 0")

    def deposit(self, amount):
        self._validate_negative_amount(amount)
        self.balance += amount

    def check_balance(self, pin):
        self._verify_pin(pin)
        return self.balance

    def withdraw(self, amount, pin):
        self._verify_pin(pin)
        self._validate_amount(amount)
        self._validate_negative_amount(amount)
        self.balance -= amount

    def _validate_amount(self, amount):
        if amount > self.balance:
            raise ValueError("Amount cannot be greater than balance")

    def _validate_negative_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

    def _validate_name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty")

    def _validate_pin(self, pin):
        pin = pin.strip()

        if pin == "" or not pin.isdigit() or len(pin) != 4:
            raise ValueError("Invalid pin")

        return pin