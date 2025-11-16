first_number = int(input("Enter a number: "))
operator = input("Enter an opeeratoor +,-,*,/: ")
second_number = int(input("Enter second number: "))

if(operator == "+"):
    print(first_number + second_number)
elif(operator == "-"):
    print(first_number - second_number)
elif(operator == "*"):
    print(first_number * second_number)
elif(operator == "/"):
    print(first_number / second_number)
else:print("Enter a valid operator")
