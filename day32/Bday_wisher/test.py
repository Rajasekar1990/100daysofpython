# """ smtplib module is used to set up a smtp server for sending mails """
# import smtplib
# import random
#
# myemail = "pythonmailtest28@gmail.com"
# mypassword = "fmcavehzstrmhseh"
# recipientemail = "pythonmailtest28@yahoo.com"
# my_msg = f"Subject:Test Email-{random.randint(0, 100)}\n\nThis is a test email from {myemail}"
# # recipient_email = smtplib.SMTP(host="smtp.mail.yahoo.com")
# with smtplib.SMTP("smtp.gmail.com") as sender_email:
#     # sender_email = smtplib.SMTP("smtp.gmail.com")  # set up the host for email provider
#     sender_email.starttls()  # secure the connection using tls b/w device and mail server
#     sender_email.login(user=myemail, password=mypassword)  # login to email account using ID and password
#     sender_email.sendmail(from_addr=myemail,
#                           to_addrs=recipientemail,
#                           msg=my_msg)  # compose mail with subject and body
#     # sender_email.close()  # close connection from your computer to mail server

import datetime as dt
current_tstamp = dt.datetime.now()
current_year = current_tstamp.year
current_month = current_tstamp.month
current_day = current_tstamp.day
current_time = str(current_tstamp.hour)+":"+str(current_tstamp.minute)+":"+str(current_tstamp.second)

dob = dt.datetime(day=1, month=1, year=1990, hour=7, minute=30, second=00)
print(dob)
print(f"{current_day}/{current_month}/{current_year} {current_time}")

day_in_week = current_tstamp.weekday()
print(day_in_week)

