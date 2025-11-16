first_integer = int(input("Enter an intege: r"))
second_integer = int(input("Enter another integer: "))
third_integer = int(input("Enter another integer: "))

largest_number = first_integer
if(largest_number < second_integer):
    largest_number = second_integer
if(largest_number < third_integer):
    largest_number = third_integer
print(largest_number, "is the largest")
