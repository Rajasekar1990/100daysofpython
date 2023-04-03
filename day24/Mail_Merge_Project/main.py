# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_list = []

with open("./Input/Names/invited_names.txt", "r") as name_read:
    for row_num in name_read:
        stripped_name = row_num.strip("\n")
        name_list.append(stripped_name)

print(name_list)

with open("./Input/Letters/starting_letter.txt", "r") as st_letter_read:
    mail_content = st_letter_read.read()
    # print(sign_updated_mail_content)

for name in name_list:
    with open(f"./Output/ReadyToSend/starting_letter_{name}", "w") as send_mail_write:
        updated_mail_content = mail_content.replace("[name]", f"{name}")
        sign_updated_mail_content = updated_mail_content.replace("Angela", "Raj")
        print(sign_updated_mail_content)
        send_mail_write.write(sign_updated_mail_content)
