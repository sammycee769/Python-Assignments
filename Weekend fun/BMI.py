weight = int(input('enter your weight: '))
height = int(input("Enter your height: "))
bmi = weight * (height * height)

if(bmi < 18.5):
    print("underweight")
elif(bmi >= 18.5 and bmi < 25):
    print("Normal")
elif(bmi >= 25 and bmi < 30):
    print("Overweight")
else:print("Obese")


