# List Comprehension Example
# numbers = [1, 2, 4]
# new_num = [(item * item) for item in numbers]
# print(new_num)
#
# str1 = "rajasekar"
# new_str = [j.upper() for j in str1]
# print(new_str)
#
# num1 = [i * 2 for i in range(1, 5)]
# print(num1)
#
# name_list = ["Alex", "Beth", "Carloine", "Dave", "Eleanor", "Freddie"]
# new_name = [k.upper() for k in name_list if len(k) > 5]
# print(new_name)

# Ex: 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
#Write your 1 line code 👇 below:
squared_numbers = [num * num for num in numbers]
# squared_numbers = [num ** 2 for num in numbers]
#Write your code 👆 above:
print(squared_numbers)
