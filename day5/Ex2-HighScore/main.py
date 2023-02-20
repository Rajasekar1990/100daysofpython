print("Welcome to Highest score calculator in the given list")
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

temp=0
for i in range(0, len(student_scores)):
  if (student_scores[i] > temp):
    temp=student_scores[i]
    print(temp)
  else:
    print(temp)

print(f"higest number in the given list is {temp}")
