age = input("What is your current age? ")
ageint=int(age)

#####method1####
lifelimitDays=(round(90*365))
#print(lifelimitDays)
lifelimitWeeks=(round(90*52))
#print(lifelimitWeeks)
lifelimitMonths=(round(90*12))
#print(lifelimitMonths)

agedDays=round(ageint*365)
#print(agedDays)
agedWeeks=round(ageint*52)
#print(agedWeeks)
agedMonths=round(ageint*12)
#print(agedMonths)

daysLeft=round(lifelimitDays-agedDays)
#print(daysLeft)
weeksLeft=round(lifelimitWeeks-agedWeeks)
#print(weeksLeft)
monthsLeft=round(lifelimitMonths-agedMonths)
#print(monthsLeft)

print(f"You have {daysLeft} days, {weeksLeft} weeks, {monthsLeft} months")

#####method2####
ageLeft=(90-round(ageint))
#print(ageLeft)

daysLeft1=round(ageLeft*365)
#print(daysLeft1)

weeksLeft1=round(ageLeft*52)
#print(weeksLeft1)

monthsLeft1=round(ageLeft*12)
#print(monthsLeft1)
print(f"You have {daysLeft1} days, {weeksLeft1} weeks, {monthsLeft1} months")