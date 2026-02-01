import Account_using_dictionary as AccountApp

while True:
    print("\nWelcome to the Bank Application")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer Funds")
    print("6. Exit")

    choice = input("Please select an option (1-6): ")

    if choice == '1':
        name = input("Enter your name: ")
        phone_number = int(input("Enter your phone number: "))
        initial_deposit = float(input("Enter initial deposit amount: "))
        pin = int(input("Set a 4-digit PIN: "))
        account = AccountApp.create_account(name, phone_number, initial_deposit, pin)
        AccountApp.add_account_to_bank(AccountApp.bank, account)
        print("Account created successfully!")
    
    elif choice == '2':
        phone_number = int(input("Enter your account number (phone number): "))
        amount = float(input("Enter deposit amount: "))
        for acc in AccountApp.bank:
            if acc["account_number"] == phone_number:
                new_balance = AccountApp.deposit(acc, amount)
                print(f"Deposit successful! New balance: {new_balance}")
                break
        else:
            print("Account not found.")
    
    elif choice == '3':
        phone_number = int(input("Enter your account number (phone number): "))
        amount = float(input("Enter withdrawal amount: "))
        pin = int(input("Enter your PIN: "))
        for acc in AccountApp.bank:
            if acc["account_number"] == phone_number:
                result = AccountApp.withdraw(acc, amount, pin)
                print(result)
                break
        else:
            print("Account not found.")
    
    elif choice == '4':
        phone_number = int(input("Enter your account number (phone number): "))
        pin = int(input("Enter your PIN: "))
        for acc in AccountApp.bank:
            if acc["account_number"] == phone_number:
                balance = AccountApp.check_balance(acc, pin)
                print(f"Your balance is: {balance}")
                break
        else:
            print("Account not found.")
    elif choice == '5':
        sender_phone = int(input("Enter your account number (phone number): "))
        receiver_phone = int(input("Enter receiver's account number (phone number): "))
        amount = float(input("Enter transfer amount: "))
        pin = int(input("Enter your PIN: "))
        sender_account = None
        receiver_account = None
        for acc in AccountApp.bank:
            if acc["account_number"] == sender_phone:
                sender_account = acc
            if acc["account_number"] == receiver_phone:
                receiver_account = acc
        if sender_account and receiver_account:
            result = AccountApp.transfer_funds(sender_account, receiver_account, amount, pin)
            print(result)
        else:
            print("One or both accounts not found.")
    
    elif choice == '6':
        print("Thank you for using the Bank Application. Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")



