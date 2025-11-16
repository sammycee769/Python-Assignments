year = int(input("Enter a year: "))
leap_year = year % 4
not_leap_year = year % 100
leap_year_two = year % 400

if(leap_year == 0 or not_leap_year != 0 or leap_year_two == 0 ):
    print("It is a leap year")
else:print("it is not a leap year")
