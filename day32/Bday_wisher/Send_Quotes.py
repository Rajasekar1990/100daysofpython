import datetime as dt
import smtplib
import random

now = dt.datetime.now()  # returns current timestamp from datetime class
day_in_week = dt.datetime.weekday(now)
print(day_in_week)

""" check for current day in this week """
if day_in_week == 1:
    with open(file="quotes.txt", mode="r") as quote_fp:
        quote_list = quote_fp.readlines()
        # print(quote_list)
        today_quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com") as gmail_smtp:
        gmail_smtp.starttls()
        gmail_smtp.login(user="pythonmailtest28@gmail.com", password="fmcavehzstrmhseh")
        gmail_smtp.sendmail(from_addr="pythonmailtest28@gmail.com",
                            to_addrs="pythonmailtest28@yahoo.com",
                            msg=f"Subject:Quote of the day\n\n"
                                f"{today_quote}")
