print("Welcome to Avg Height Calculator in the given list")
student_heights=input("Enter the list of student heights ").split()
print(student_heights)
#student_heights = [180, 124, 165, 173, 189, 169, 146]

for i in range(0, len(student_heights)):
    student_heights[i]=int(student_heights[i])
    # print(student_heights[i])
    # print(type(student_heights[i]))

total=0
count=0

for j in student_heights:
    total+=j
    count+=1
print(total)
print(count)

avg=round(total/count)

print(f"Average height rounded to the nearest whole number = {avg}")
