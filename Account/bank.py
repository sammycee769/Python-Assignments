from account import Account


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, pin, name, phone_number):
        account_number = self._create_account_number(phone_number)
        self._duplicate_account_validator(account_number)

        new_account = Account(pin, name, phone_number)
        new_account.set_account_number(account_number)

        self.accounts.append(new_account)

    def _create_account_number(self, phone_number):
        self._verify_phone_number(phone_number)
        return phone_number[1:]

    def get_number_of_accounts(self):
        return len(self.accounts)

    def _verify_phone_number(self, phone_number):
        phone_number = phone_number.strip()

        if phone_number == "":
            raise ValueError("Phone number cannot be empty")

        if len(phone_number) != 11:
            raise ValueError("Phone number must be 11 characters long")

        if not phone_number.isdigit():
            raise ValueError("Phone number must be exactly 11 digits")

        if not phone_number.startswith("0"):
            raise ValueError("Phone number must start with 0")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        self._validate_account(account)
        account.deposit(amount)

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        self._validate_account(account)
        return account.check_balance(pin)

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        self._validate_account(account)
        account.withdraw(amount, pin)

    def transfer(self, sender_number, receiver_number, amount, pin):
        sender = self.find_account(sender_number)
        receiver = self.find_account(receiver_number)

        self._validate_transfer(sender, receiver)

        sender.withdraw(amount, pin)
        receiver.deposit(amount)

    def _validate_transfer(self, sender, receiver):
        if sender is None:
            raise ValueError("Sender account not found")

        if receiver is None:
            raise ValueError("Recipient account not found")

        if sender == receiver:
            raise ValueError("Sender and receiver cannot be same")

    def _validate_account(self, account):
        if account is None:
            raise ValueError("Account not found")

    def _duplicate_account_validator(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                raise ValueError("Account already exists")