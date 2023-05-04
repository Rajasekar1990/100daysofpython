import time
import requests
import datetime as dt
import smtplib

MY_LAT = -20.01245
MY_LNG = 176.594566
my_email = "pythonmailtest28@gmail.com"  # Your email id from where you want to send an email
my_password = "fmcavehzstrmhseh"  # Your password for where you want to send an email (App Password)


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    if (latitude - 5) <= MY_LAT <= (latitude + 5) and (longitude - 5) <= MY_LNG <= (longitude + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    result = response.json()
    print(result)
    sunrise_hour = int(result["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(result["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise_hour, sunset_hour)

    now = dt.datetime.now()
    hour = now.hour
    print(hour)

    if hour >= sunset_hour or hour <= sunrise_hour:
        return True


while True:
    time.sleep(1)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="satheeshpandianj@gmail.com",
                                msg="Sub: ISS Navigation is up in the sky, Look Up\n\n Hey, look up the sky to see ISS navigation")
