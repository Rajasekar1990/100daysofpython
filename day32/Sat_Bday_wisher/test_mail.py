import datetime as dt
import random
import smtplib

# now = dt.datetime.now()
# print(now.weekday())
# if now.weekday() == 1:
#     with open("quotes.txt", "r") as data:
#         file = data.readlines()
#         random_quote = random.choice(file)
#         # print(random_quote)
#         print(random_quote)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         my_email = "satheeshpandianj@gmail.com"
#         my_password = "yybwtqphmnsworow"
#
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="satsqaexperience@gmail.com",
#                             msg=f"Sub: Quote of the day \n\n {random_quote}")

import pandas
import datetime as dt
import smtplib

NAME="[NAME]"
my_email = "satheeshpandianj@gmail.com"
my_password = "yybwtqphmnsworow"

now = dt.datetime.now()
# print(now)
month = now.month
day = now.day

# print(month, day)
data = pandas.read_csv("birthdays.csv")
# print(data)
new_list = data.to_dict(orient="records")
# print(new_list)
# print(type(new_list))
for item in new_list:
    if item["month"] == month and item["day"] == day:
        name = item["name"]
        email = item["email"]
        # print(name, email)

        with open("letter_templates/letter_1.txt") as file:
            content = file.read()
            # print(content)
            replace_name = content.replace(NAME, f"{name}")
            # print(replace_name)
            print(replace_name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
            to_addrs=email,
            msg=f"Sub: Happy Birthday \n\n {replace_name}")