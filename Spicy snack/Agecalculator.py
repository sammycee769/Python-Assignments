fathers_current_age = int(input("Enter father's current age: "))
sons_current_age = int(input("Enter son's current age: "))
years_ago = 2 * sons_current_age - fathers_current_age


if (fathers_current_age or sons_current_age > 0) and (fathers_current_age or sons_current_age < 81):
    print(abs(years_ago))
else:print("Enter an age between 1 and 80")
