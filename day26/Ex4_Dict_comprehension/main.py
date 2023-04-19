import pandas
import random

my_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# dictionary comprehension examples
my_dict = {list_item: random.randint(0, 100) for list_item in my_list}
print(my_dict)
print(my_dict.items())

# method 1:
pass_cand = {key: my_dict[key] for key in my_dict if my_dict[key] >= 60}
print(pass_cand)

# method 2:
# pass_can = {new_key: new_value for (key, value) in dictionary.items() if value >= 60}
pass_cand1 = {student: score for (student, score) in my_dict.items() if score >= 60}
print(pass_cand1)

# Exercise 1
sentence = "what is the Airspeed Velocity of Unladen Swallow?"
# Don't change the code above
# Write your code below:
# sentence = sentence.split()
# print(sentence)
word_count = {word: len(word) for word in sentence.split()}
print(word_count)

# Exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def c_to_f(temp_c):
    temp_f = round((temp_c * (9 / 5)) + 32, 1)
    return temp_f


weather_f = {day: c_to_f(celcius) for (day, celcius) in weather_c.items()}
print(weather_f)
weather_f = {day: round((weather_c[day] * (9 / 5)) + 32, 1) for day in weather_c}
print(weather_f)
weather_f = {day: round((temp_c * (9 / 5)) + 32, 1) for (day, temp_c) in weather_c.items()}
print(weather_f)

# dictionary comprehension using pandas lib
students_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [60, 75, 90]
}

# normal looping with dictionary
# for (student_name, score) in students_dict.items():
#     print(score)

students_data_frame = pandas.DataFrame(students_dict)
print(students_data_frame)

# Looping through Dataframe
# for (name, marks) in students_data_frame.items():
#     print(marks)

# pandas having inbuilt looping called iterrows() method
for (index, row) in students_data_frame.iterrows():
    if row.student == "James": print(row.score)
