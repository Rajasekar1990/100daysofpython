import requests
import datetime as dt

LAT = 12.9767936
LNG = 77.590082

""" Get current time """
current_time = dt.datetime.now()
print(current_time)
current_hour = current_time.hour
print(current_hour)

""" url query string parameters """
parameters = {"lat": LAT,  # as float (required)
              "lng": LNG,  # as float (required)
              "formatted": 0  # returns timestamp in unix version (optional)
              }

sun_rise_set = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sun_rise_set.raise_for_status()
response_data = sun_rise_set.json()
# print(response_data)
sun_rise = response_data["results"]["sunrise"].split('T')[1].split(':')[0]
print(f"sunrise hour is : {sun_rise}")
sun_set = response_data["results"]["sunset"].split('T')[1].split(':')[0]
print(f"sunset hour is : {sun_set}")

""" to find whether it is day or night; just compare the current hour in your loc with sunrise/sunset """
if int(sun_rise) <= int(current_hour) <= int(sun_set):
    print("It is day!")
else:
    print("It is night!")
