from bank import Bank


class AtmMachine:

    def __init__(self):
        self.bank = Bank("Christian Fake Bank")

    def start(self):
        while True:
            self.display_main_menu()

    def display_main_menu(self):

        print("""
Welcome to Christian Fake Bank!!!
1 -> Create Account
2 -> Deposit
3 -> Withdraw
4 -> Transfer
5 -> Check Balance
6 -> Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            self.create_account()

        elif choice == "2":
            self.deposit()

        elif choice == "3":
            self.withdraw()

        elif choice == "4":
            self.transfer()

        elif choice == "5":
            self.check_balance()

        else:
            print("Goodbye")
            exit()

    def create_account(self):
        try:
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            pin = input("Enter Pin: ")

            self.bank.create_account(pin, name, phone)

            print("Account created successfully")

        except Exception as e:
            print(e)

    def deposit(self):
        try:
            account_number = input("Enter Account Number: ")
            amount = int(input("Enter Amount: "))

            self.bank.deposit(account_number, amount)

            print("Deposit successful")

        except Exception as e:
            print(e)

    def withdraw(self):
        try:
            account_number = input("Enter Account Number: ")
            pin = input("Enter Pin: ")
            amount = int(input("Enter Amount: "))

            self.bank.withdraw(account_number, amount, pin)

            balance = self.bank.check_balance(account_number, pin)

            print("Withdraw successful")
            print("New balance:", balance)

        except Exception as e:
            print(e)

    def transfer(self):
        try:
            sender = input("Sender Account: ")
            receiver = input("Receiver Account: ")
            pin = input("Enter Pin: ")
            amount = int(input("Enter Amount: "))

            self.bank.transfer(sender, receiver, amount, pin)

            balance = self.bank.check_balance(sender, pin)

            print("Transfer successful")
            print("New balance:", balance)

        except Exception as e:
            print(e)

    def check_balance(self):
        try:
            account_number = input("Enter Account Number: ")
            pin = input("Enter Pin: ")

            balance = self.bank.check_balance(account_number, pin)

            print("Balance:", balance)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    atm = AtmMachine()
    atm.start()