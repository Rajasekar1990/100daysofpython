import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
           "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
final_password_list = []

for num_letters in range(1, random.randint(8, 32)):
    final_password_list.append(random.choice(letters))

# print(final_password_list)
# print(len(final_password_list))
final_password = "".join(final_password_list)
print(final_password)
print(len(final_password))

