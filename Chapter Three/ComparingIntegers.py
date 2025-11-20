print('Enter two integers, and I will tell you',
'the relationships they satisfy.')

number_one = int(input('Enter first integer: '))
number_two = int(input('Enter second integer: '))

if(number_one == number_two):
    print(number_one,"is equal to",number_two)
else:print(number_one,"is not equal to",number_two)
if (number_one < number_two):
    print(number_one,"is less than ",number_two)
else:print(number_one, 'is greater than', number_two)
if(number_one <= number_two):
    print(number_one, 'is less than or equal to', number_two)
else:print(number_one, 'is greater than or equal to', number_two)
