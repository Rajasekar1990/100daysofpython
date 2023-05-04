import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 10.4729  # Your latitude
MY_LONG = 45.1263  # Your longitude
MY_EMAIL = "pythonmailtest28@gmail.com"
MY_PASSWORD = "fmcavehzstrmhseh"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (iss_latitude - 5) <= MY_LAT <= (iss_latitude + 5) or \
            (iss_longitude - 5) <= MY_LAT <= (iss_longitude + 5):
        return True
    else:
        return False


def is_night_check():
    is_night_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    is_night_response.raise_for_status()
    is_night_data = is_night_response.json()
    print(is_night_data)
    sunrise = int(is_night_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(is_night_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour
    print(f"Sunrise hour: {sunrise}")
    print(f"Sunset hour: {sunset}")
    print(f"Current Hour: {current_hour}")

    if int(sunrise) <= int(current_hour) >= int(sunset):
        print("It's a day")
        return False
    else:
        print("Currently dark")
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def email_note():
    # print(is_iss_overhead())
    # print(is_night_check())
    if is_iss_overhead() and is_night_check():
        send_email = smtplib.SMTP("smtp.gmail.com")
        send_email.starttls()
        send_email.login(user=MY_EMAIL, password=MY_PASSWORD)
        send_email.sendmail(from_addr=MY_EMAIL,
                            to_addrs="pythonmailtest28@yahoo.com",
                            msg=f"Subject: ISS IS OVERHEAD\n\n"
                                f"Hey, look up in the sky!")


while True:
    email_note()
    time.sleep(5)
