
bank = []

def create_account(name, phone_number, initial_deposit, pin):
    return {
        "name": name,
        "account_number": phone_number,
        "balance": initial_deposit,
        "pin": pin
    }

def add_account_to_bank(bank, account):
    bank.append(account)
    return bank

def deposit(account, amount):
    account["balance"] += amount
    return account["balance"]
    
def withdraw(account, amount, pin):
    if pin != account["pin"]:
        return "Invalid PIN"

    if amount > account["balance"] or account["balance"] - amount <= 100:
        return "Insufficient funds"

    account["balance"] -= amount
    return "Withdrawal successful",account["balance"]


def check_balance(account, pin):
    if pin == account["pin"]:
        return account["balance"]
    else:
        return "Invalid PIN"

def transfer_funds(sender_account, receiver_account, amount, pin):
    if pin != sender_account["pin"]:
        return "Invalid PIN"
    if amount > sender_account["balance"] or sender_account["balance"]-amount <= 100:
        return "Insufficient funds"
    if sender_account["account_number"] == receiver_account["account_number"]:
        return "Cannot transfer to the same account"
    if amount > sender_account["balance"]:
        return "Insufficient funds"
    sender_account["balance"] -= amount
    receiver_account["balance"] += amount
    return "Transfer successful"



