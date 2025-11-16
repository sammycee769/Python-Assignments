first_grade = int(input("Enter first grade: "))
second_grade = int(input("Enter second Grade: "))
third_grade = int(input("Enter third grade: "))
average_grade = (first_grade + second_grade + third_grade) / 3
if(90 <= average_grade and average_grade <= 100):
    print("Your grade is A")
elif(80 <= average_grade and average_grade < 90):
    print("Your grade is B")
elif(70 <= average_grade and average_grade < 80):
    print("Your grade is C")
elif(60 <= average_grade and average_grade < 70):
    print("Your grade is D")
else:print("Your grade is F")
