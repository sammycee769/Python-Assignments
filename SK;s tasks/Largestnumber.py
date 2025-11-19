largest_number = 0
small_numbers = 0
sentinel = 0
user_input = int(input("Enter any number (Enter 0 to exit): "))

while(user_input != sentinel):
    if(user_input > largest_number):
        largest_number = user_input
    else:small_numbers = user_input
    user_input = int(input("Enter any number (Enter 0 to exit): "))

#print("Enter any number (Enter 0 to exit): ")
print(f"The largest number is {largest_number}")
print(f"The small number is {small_numbers}")
