weight=input("Enter your weight in Kg ")
height=input("Enter your height in m ")

bmi=round((float(weight)/(float(height)**2)),1)

#method1:
if (bmi <= 18.5):
    print(f"Your BMI is {bmi}, You are underweight")
elif (bmi > 18.5 and bmi <= 25):
    print(f"Your BMI is {bmi}, Yous is a normal weight")
elif (bmi > 25 and bmi <= 30):
    print(f"Your BMI is {bmi}, You are slightly overweight")
elif (bmi > 30 and bmi <= 35):
    print(f"Your BMI is {bmi}, You are obese")
else:
    print(f"Your BMI is {bmi}, You are clinically obese")

#method2:
if (bmi < 18.5):
    print(f"Your BMI is {bmi}, You are underweight")
elif (bmi < 25):
    print(f"Your BMI is {bmi}, Yous is a normal weight")
elif (bmi < 30):
    print(f"Your BMI is {bmi}, You are slightly overweight")
elif (bmi < 35):
    print(f"Your BMI is {bmi}, You are obese")
else:
    print(f"Your BMI is {bmi}, You are clinically obese")
