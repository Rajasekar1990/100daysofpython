import random
import pandas

csv_data = pandas.read_csv("./data/french_words.csv")
# french_word_dict = csv_data.to_dict()  # prints the complete set of data in the form of nested dict
# print(french_word_dict)
french_word_dict = csv_data.to_dict(orient="records")  # prints the data in the form dictionary inside list
print(french_word_dict)


def randomly_picked_word():
    new_dict = random.choice(french_word_dict)
    print(new_dict)
    title = new_dict["French"]
    word = new_dict["English"]
    print(f"{title} = {word}")


randomly_picked_word()
