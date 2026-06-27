Name=input("Enter your name: ")
weight= float(input("Enter your weight in kilograms: "))
print(weight)
height= float(input("Enter your height in meters: "))
print(height)
bmi= (weight) / (height*height)
print("Your BMI IS :", bmi) 
bmi= float(input("Enter your BMI: "))
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
elif bmi >= 30:
    print("You are obese.")
elif bmi >= 35:
    print("You are severely obese.")
else:
    print("You are morbidly obese.")


input("press enter to exit ")
