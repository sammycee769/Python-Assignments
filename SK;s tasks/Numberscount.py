positive_numbers = 0
negative_numbers = 0
zero = 0
centinel = -1
user_input = int(input("enter a number or enter -1 to quit "))

while(user_input != centinel):
    if(user_input < 0):
        negative_numbers += 1
    elif(user_input > 0):
        positive_numbers += 1
    else:zero += 1
    user_input = int(input("enter a number or enter -1 to quit "))
print(f"the positive numbers count are {positive_numbers},the negative numbers count are {negative_numbers} and the zero counts are {zero} ")
