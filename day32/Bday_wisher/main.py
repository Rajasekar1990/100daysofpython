import smtplib
import datetime as dt
import pandas
import random

""" setting up mail server """
user_name = "pythonmailtest28@gmail.com"
password = "fmcavehzstrmhseh"

""" retrieving current timestamp using datatime class """
current_tstamp = dt.datetime.now()
current_month = current_tstamp.month
current_day = current_tstamp.day

""" Creating list dictionary as csv data contains dict inside a dictionary """
csv_data = pandas.read_csv("birthdays.csv")
print(csv_data)

# my_dict = csv_data.to_dict() # nested dict
# print(my_dict)
my_list_dict = csv_data.to_dict(orient="records")
print(my_list_dict)

""" looping through list dict to get dictionary having name, email, dob """
for item in my_list_dict:
    bday_person = item["name"]
    to_addr = item["email"]
    bday_month = item["month"]
    bday_day = item["day"]

    if current_month == bday_month and current_day == bday_day:
        """ read letter_x.txt for composing body content """
        with open(file=f"letter_{random.randint(1,3)}.txt", mode="r") as mail_content:
            mail_content_list = mail_content.readlines()
            # print(mail_content_list)
            mail_content_str = "".join(mail_content_list)
            # print(mail_content_str)
            updated_mail_content = mail_content_str.replace("[NAME]", f"{bday_person}")
            # print(updated_mail_content)

        with smtplib.SMTP("smtp.gmail.com") as send_email:
            send_email.starttls()
            send_email.login(user=user_name, password=password)
            send_email.sendmail(from_addr=user_name,
                                to_addrs=to_addr,
                                msg=f"Subject: Happy Birthday {bday_person}!!!\n\n"
                                    f"{updated_mail_content}")
