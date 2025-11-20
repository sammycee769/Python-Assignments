amount = float(input("Enter your principal: "))
#number_of_years = int(input("Enter the years: "))
interest_rate = float(input("enter your interest rate: "))

print("Year \t Rate \t ROI")
for year in range(1,31) :

    rate_on_roi = (interest_rate / 100) * amount
    roi = amount * ((1+interest_rate) ** year)
    amount = roi
    print(f"{year}\t {interest_rate}\t{amount}")
