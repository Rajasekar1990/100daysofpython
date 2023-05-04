import requests


MY_LAT = 13.0827
MY_LONG = 80.2707
""" Response code: 1xx - hold on 2xx - Here you go 3xx - Go away 4xx - You are screwed up 5xx - server is screwed up """

iss_api_response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(iss_api_response)  # returns the http status code of the end point been hit
print(iss_api_response.status_code) # returns only the http status code

# if iss_api_response.status_code == 200:
#     print("Success/OK")
# elif iss_api_response.status_code == 404:
#     raise Exception ("URL not found") # raise an exception with a specific message

iss_api_response.raise_for_status()  # raise exception based on the http response code
response_data = iss_api_response.json()
print(response_data)

current_latitude = response_data["iss_position"]["latitude"]
current_longitude = response_data["iss_position"]["longitude"]
iss_current_location = (current_latitude, current_longitude)
print(iss_current_location)



