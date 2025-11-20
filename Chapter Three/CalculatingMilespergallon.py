gallon_used = float(input("Enter the gallons used (-1 to end): "))
miles_covered = float(input("Enter the miles driven: "))
gallons_usedtwo = 0
while(gallon_used != -1 ):
    gallons_usedtwo += 1
    miles_gallon = miles_covered / gallon_used
    overall_average = miles_gallon / gallons_usedtwo
    gallon_used = float(input("Enter the gallons used (-1 to end): "))
    miles_covered = float(input("Enter the miles driven: "))
    print("The miles/gallon for this tank was",miles_gallon )

print("The overall average miles/gallon was",overall_average)
