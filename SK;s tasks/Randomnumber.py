import random
random_number = random.randint(1,10)
user_input = int(input("Enter a numer betweeen 1 and 1o: "))
while(user_input != random_number):
    if(user_input > random_number):
        print("Too high;try again: ")
    elif(user_input < random_number):
        print("too low,try again: ")
    user_input = int(input("Enter a numer betweeen 1 and 1o: "))
print("Correct")
    
