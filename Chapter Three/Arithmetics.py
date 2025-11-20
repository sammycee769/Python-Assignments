smallest_number = 100 **1000000
largest_number = 0
#average_number = 0
product = 1
addition = 0
for number in range(4):
    
    user_input = int(input("Enter a number: "))
    product *= user_input
   
    addition += user_input
    average = addition / 4
    if(user_input > largest_number):
        largest_number = user_input
    if(user_input < smallest_number):
        smallest_number = user_input
print(f"The sum of the values are {addition} the product is {product} the average {average} the smallest {smallest_number} and the largest number {largest_number}")
    
