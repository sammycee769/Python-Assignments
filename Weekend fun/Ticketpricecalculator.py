age = int(input("Enter your age: "))

if(age < 5):
    print('ticket is free.')
elif(age >4 and age <13):
    print("ticket price is $5")
elif(age >12 and age <65):
    print("ticket price is $12")
else:print("ticket price is $8")
