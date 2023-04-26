import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # print(index)
#     # print(row)
#     # Access row.student or row.score
#     if row.student == "Angela":
#         print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
data_dict = data.to_dict()
# print(data_dict)
data_frame = pandas.DataFrame(data_dict)
# print(data_frame)

# Creating a new dictionary called my_dict to store alphabet: word
""" Using Dictionary comprehension """
my_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}
print(my_dict)

""" Looping through dictionary frame with iterrows method """


# for (index, row) in data_frame.iterrows():
#     my_dict[row.letter] = row.code
# print(my_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# my_list = []

# Method 1 using while loop to ask for user input
# continue_check = True
# while continue_check:
#     user_input = input("Enter the word: ").upper()
#     if user_input == "EXIT":
#         continue_check = False
#     else:
#         """ Using list comprehension """
#         try:
#             my_list = [my_dict[word] for word in [char for char in user_input]]
#             """ Looping through dictionary and append the outcome in my_list """
#             # for letter in [char for char in user_input]:
#             #     my_list.append(my_dict[letter])
#         except KeyError:
#             print("Sorry. Only letters in the alphabets please.")
#             # continue_check = True
#         else:
#             print(my_list)

# Method 2: Using a function to ask for user input until exit
def nato_gen():
    user_input = input("Enter the word: ").upper()
    if user_input == "EXIT":
        exit()
    try:
        my_list = [my_dict[word] for word in [char for char in user_input]]
    except KeyError:
        print("Sorry. Only letters in the alphabets please.")
        nato_gen()
    else:
        print(my_list)
        nato_gen()


nato_gen()
