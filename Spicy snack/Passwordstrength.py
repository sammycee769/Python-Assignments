password = input("enter password")

if(len(password) > 6 and len(password) <= 10):
    print("Strong")
elif(len(password) < 6 and len(password) > 1):
    print("Weak")
elif(len(password) > 10):
    print("Strong")
elif(len(password) < 1):
    print("password is invalid")
else:print("password is invalid")
