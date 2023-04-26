""" Generic Error Types """
""" 1. File Not Found """
""" 2. Key Error """
""" 3. Type Error """
""" 4. Value Errors using raise to handle with custom error message """

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:  # one or more except to react with error handling
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:  # will execute only when try succeeds
#     content = file.read()
#     print(content)
# finally:  # will execute whether try succeeds or fails
#     raise TypeError("This is an error that I made up.")
#
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.") #
#
# bmi = weight / height ** 2
# print(bmi)

""" Coding Exercise 1 - Index error handling """
# fruits = ["Apple", "Pear", "Orange"]
# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
# make_pie(4)

""" Coding Exercise 2 - Key error handling """
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        # total_likes += 0
        pass
    else:
        pass
print(total_likes)