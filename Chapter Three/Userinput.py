passes = 0
failures = 0

user_input = int(input("Enter any number (50+ = pass, 49 below = fail, 1 0r 2 to stop ): "))

while(user_input != 1 and user_input != 2):
    if(user_input >= 50):
        passes +=1
    else:failures +=1
    user_input = int(input("Enter any number (50+ = pass, 49 below = fail,1 0r 2 to stop): "))
print(f"The number of passes are {passes}")
print(f"The number of failures are {failures}")
