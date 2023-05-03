##################### Normal Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random

username = "pythonmailtest28@gmail.com"
password = "fmcavehzstrmhseh"

current_time = dt.datetime.now()
today_tuple = (current_time.month, current_time.day)
print(today_tuple)

data = pandas.read_csv("birthdays.csv")
print(data)

# my_dict = {}
# for (index, row) in data.iterrows():
#     my_dict["email"] = row.email
#     my_dict["name"] = row.name
#
# print(my_dict)
birthdays_dict = {(data_row.month, data_row.day): data_row
                  for (index, data_row) in data.iterrows()}
print(birthdays_dict)

for today_tuple in birthdays_dict:
    """access the values of birthdays_dict with today's tuple as key and store the values in list such as email,year."""
    birthday_list = birthdays_dict[today_tuple]
    print(birthday_list)
    with open(file=f"letter_{random.randint(1, 3)}.txt", mode="r") as mail_body:
        content = mail_body.readlines()
        content_str = "".join(content)
        updated_content = content_str.replace("[NAME]", birthday_list["name"])

    with smtplib.SMTP("smtp.gmail.com") as sender_mail:
        sender_mail.starttls()
        sender_mail.login(user=username, password=password)
        sender_mail.sendmail(from_addr=username,
                             to_addrs=f"{birthday_list['email']}",
                             msg=f"Subject: Happy B'day {birthday_list['name']}!!!\n\n"
                                 f"{updated_content}")
