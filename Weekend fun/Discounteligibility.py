total_bill = int(input("Enter your total bill: "))
is_member = input("Are you a member yes/no: ")

if(total_bill >= 1000 and is_member == "yes"):
    print("10% off")
elif(total_bill >= 1000 and is_member != "yes"):
    print("5% off")
else:print("no discount on ", total_bill)
