age = input("What is your current age? ")
ageint=int(age)

#####method1####
lifelimitDays=90*365
#print(lifelimitDays)
lifelimitWeeks=90*52
#print(lifelimitWeeks)
lifelimitMonths=90*12
#print(lifelimitMonths)

agedDays=ageint*365
#print(agedDays)
agedWeeks=ageint*52
#print(agedWeeks)
agedMonths=ageint*12
#print(agedMonths)

daysLeft=lifelimitDays-agedDays
#print(daysLeft)
weeksLeft=lifelimitWeeks-agedWeeks
#print(weeksLeft)
monthsLeft=lifelimitMonths-agedMonths
#print(monthsLeft)

print(f"You have {daysLeft} days, {weeksLeft} weeks, {monthsLeft} months")

#####method2####
ageLeft=90-ageint
#print(ageLeft)

daysLeft1=ageLeft*365
#print(daysLeft1)

weeksLeft1=ageLeft*52
#print(weeksLeft1)

monthsLeft1=ageLeft*12
#print(monthsLeft1)
print(f"You have {daysLeft1} days, {weeksLeft1} weeks, {monthsLeft1} months")