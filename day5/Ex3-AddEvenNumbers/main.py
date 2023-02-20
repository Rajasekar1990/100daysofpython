print("Add Even Numbers")
SUM=int(input("To which number you want add the even numbers? "))

totalevennumbers=0
for i in range (1,SUM+1):
    if (i % 2 == 0):
        totalevennumbers+=i
print(totalevennumbers)

totalevennumbers1=0
for j in range (2,SUM+1,2):
    totalevennumbers1+=j
print(totalevennumbers1)