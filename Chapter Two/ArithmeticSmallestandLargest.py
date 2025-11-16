number_one = int(input("Enter a number: "))
number_two = int(input("Enter another number: "))
number_three = int(input("Enter another number: "))
sum_of_numbers = number_one + number_two + number_three
average_of_numbers = sum_of_numbers / 3
product_of_numbers = number_one * number_two * number_three
largest_number = number_one
smallest_number = number_one

#if(number_one > number_two or number_one > number_three):
#   largest_number = 
#elif(number_two > number_one or number_two > number_three):
#    print(f"{number_two} is the largest number")
#elif(number_three > number_one or number_three > number_two):
#    print(f"{number_three} is the largest number")
#    print(f"{number_one} is the largest number, {average_of_numbers} ")
if(largest_number < number_two):
    largest_number = number_two
if(largest_number < number_three):
    largest_number = number_three
if(smallest_number > number_two):
    smallest_number = number_two
if(smallest_number > number_three):
    smallest_number = number_three
print(f"{largest_number} is the largest number,{smallest_number} is the smallest number,{sum_of_numbers} is the sum of the numbers, {average_of_numbers} is the average and {product_of_numbers} is the product")
