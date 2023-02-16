weight=input("Enter your weight in Kg ")
height=input("Enter your height in m ")

bmi=(float(weight)/(float(height)**2))
print(type(bmi))
bmi=int(bmi)
print(type(bmi))
print("Your BMI is " + str(bmi))