number = int(input("Enter a five digit number"))
first_digit = number // 10000
second_digit =(number // 1000) %10
third_digit = (number // 100) % 10
fourth_digit = (number % 100) // 10
fifth_digit = number % 10;

if(number > 9999 and number < 999999):
    print(fifth_digit,fourth_digit,third_digit,second_digit,first_digit)
