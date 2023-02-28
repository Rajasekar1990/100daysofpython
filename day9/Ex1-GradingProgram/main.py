#Welcome to Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for student_name in student_scores:
    score=int(student_scores[student_name])
    if(score > 90):
       student_grades[student_name]="Outstanding" 
    elif(score > 80):
       student_grades[student_name]="Exceeds Expectations" 
    elif(score > 70):
       student_grades[student_name]="Acceptable"
    else:
       student_grades[student_name]="Fail"
    
print(student_grades)